import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

st.set_page_config(page_title="Customer Analytics", layout="wide")
st.title("👥 Customer Analytics & RFM Segmentation")

BASE_DIR = Path(__file__).resolve().parent.parent.parent
data_path = BASE_DIR / "processed" / "RetailPulse_Cleaned_Transactions.csv"

if data_path.exists():
    df = pd.read_csv(data_path)
    
    # Auto-detect column names dynamically
    cust_col = next((col for col in ['CustomerID', 'Customer_ID', 'Customer ID'] if col in df.columns), None)
    inv_col = next((col for col in ['InvoiceNo', 'Invoice_No', 'Invoice', 'InvoiceNumber'] if col in df.columns), None)
    price_col = next((col for col in ['TotalPrice', 'Total_Price', 'Price', 'Amount'] if col in df.columns), df.columns[0])
    
    if cust_col and inv_col:
        cust_df = df.groupby(cust_col).agg(
            TotalSpend=(price_col, 'sum'),
            OrderCount=(inv_col, 'nunique')
        ).reset_index()
        
        fig = px.scatter(
            cust_df, 
            x='OrderCount', 
            y='TotalSpend', 
            title="Customer Spend vs Order Frequency", 
            hover_data=[cust_col]
        )
        st.plotly_chart(fig, use_container_width=True)
    elif cust_col:
        cust_df = df.groupby(cust_col)[price_col].sum().reset_index()
        fig = px.bar(cust_df.head(20), x=cust_col, y=price_col, title="Top Customer Spend ($)")
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning("Customer data format preview:")
        st.dataframe(df.head(50), use_container_width=True)
else:
    st.error("Data file missing at processed/RetailPulse_Cleaned_Transactions.csv")
    import streamlit as st

# Custom Dashboard Styling
st.markdown("""
<style>
/* Main Header Gradient Styling */
.page-title {
    font-size: 2.5rem;
    font-weight: 800;
    background: linear-gradient(135deg, #00F5D4, #7B2CBF, #FF007A);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 5px;
}

/* Metric Cards Custom Styling */
div[data-testid="stMetric"] {
    background: rgba(255, 255, 255, 0.05);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 12px;
    padding: 15px;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.2);
    transition: transform 0.2s ease-in-out;
}

div[data-testid="stMetric"]:hover {
    transform: translateY(-5px);
    border-color: #00F5D4;
}

/* Tab Headers Styling */
button[data-baseweb="tab"] {
    font-weight: 600;
    font-size: 1rem;
}
</style>
""", unsafe_allow_html=True)