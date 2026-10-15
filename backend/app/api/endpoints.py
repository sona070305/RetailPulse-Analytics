from fastapi import APIRouter, HTTPException
import pandas as pd
from pathlib import Path

router = APIRouter()

BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
TX_PATH = BASE_DIR / "processed" / "RetailPulse_Cleaned_Transactions.csv"
RFM_PATH = BASE_DIR / "processed" / "Customer_RFM_Segments.csv"

@router.get("/kpis")
def get_executive_kpis():
    if not TX_PATH.exists() or not RFM_PATH.exists():
        raise HTTPException(status_code=404, detail="Processed CSV datasets not found.")
    
    df_tx = pd.read_csv(TX_PATH)
    df_rfm = pd.read_csv(RFM_PATH)
    
    total_revenue = float(df_tx['TotalPrice'].sum())
    total_orders = int(df_tx['Invoice'].nunique())
    avg_order_value = total_revenue / total_orders if total_orders > 0 else 0.0
    active_customers = int(df_rfm['CustomerID'].nunique())
    at_risk_count = int((df_rfm['Churn_Probability'] >= 0.70).sum())
    
    return {
        "total_revenue": round(total_revenue, 2),
        "total_orders": total_orders,
        "avg_order_value": round(avg_order_value, 2),
        "active_customers": active_customers,
        "at_risk_customers": at_risk_count
    }

@router.get("/sales-trends")
def get_sales_trends():
    if not TX_PATH.exists():
        raise HTTPException(status_code=404, detail="Transaction data file not found.")
    
    df_tx = pd.read_csv(TX_PATH)
    monthly = df_tx.groupby('YearMonth')['TotalPrice'].sum().reset_index()
    return monthly.to_dict(orient="records")