import pandas as pd
import numpy as np
import os
from pathlib import Path

# 1. Paths Setup (Dynamic Path Resolution)
BASE_DIR = Path(__file__).resolve().parent.parent
raw_path = BASE_DIR / "raw" / "online_retail_II.csv"
output_dir = BASE_DIR / "processed"
os.makedirs(output_dir, exist_ok=True)

# 2. Ingest Raw Data
df = pd.read_csv(raw_path, encoding='ISO-8859-1')

# 3. Step 2: Data Cleaning
df = df.dropna(subset=['Customer ID'])
df['Customer ID'] = df['Customer ID'].astype(int)
df = df[~df['Invoice'].astype(str).str.startswith('C')]  # Remove returns
df = df[(df['Quantity'] > 0) & (df['Price'] > 0)]        # Remove invalid transactions

# 4. Step 3: Create New Columns
df['TotalPrice'] = df['Quantity'] * df['Price']
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
df['YearMonth'] = df['InvoiceDate'].dt.to_period('M').astype(str)
df['DayName'] = df['InvoiceDate'].dt.day_name()
df['HourOfDay'] = df['InvoiceDate'].dt.hour

# 5. RFM Segmentation & Churn Scoring
snapshot_date = df['InvoiceDate'].max() + pd.Timedelta(days=1)
rfm = df.groupby('Customer ID').agg({
    'InvoiceDate': lambda x: (snapshot_date - x.max()).days,
    'Invoice': 'nunique',
    'TotalPrice': 'sum'
}).reset_index()

rfm.columns = ['CustomerID', 'Recency', 'Frequency', 'Monetary']
rfm['R_Score'] = pd.qcut(rfm['Recency'], 4, labels=[4, 3, 2, 1])
rfm['F_Score'] = pd.qcut(rfm['Frequency'].rank(method='first'), 4, labels=[1, 2, 3, 4])
rfm['M_Score'] = pd.qcut(rfm['Monetary'], 4, labels=[1, 2, 3, 4])

def assign_segment(row):
    r, f = int(row['R_Score']), int(row['F_Score'])
    if r >= 3 and f >= 3: return 'Champions / Loyal'
    elif r >= 2 and f >= 2: return 'Potential Loyalists'
    elif r == 1 and f >= 2: return 'At Risk / Need Attention'
    else: return 'Lost Customers'

rfm['Segment_Name'] = rfm.apply(assign_segment, axis=1)
rfm['Churn_Probability'] = np.where(rfm['Recency'] > 90, 0.85, 
                           np.where(rfm['Recency'] > 30, 0.40, 0.10))

# 6. Export Cleaned CSV Files
df.to_csv(f"{output_dir}/RetailPulse_Cleaned_Transactions.csv", index=False)
rfm.to_csv(f"{output_dir}/Customer_RFM_Segments.csv", index=False)
print("Pipeline execution complete! Cleaned files exported to /processed")