import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(page_title="Order Transactions", layout="wide")
st.title("🧾 Transaction Data Explorer")

BASE_DIR = Path(__file__).resolve().parent.parent.parent
data_path = BASE_DIR / "processed" / "RetailPulse_Cleaned_Transactions.csv"

if data_path.exists():
    df = pd.read_csv(data_path)
    st.dataframe(df.head(100), use_container_width=True)
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