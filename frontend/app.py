import streamlit as st
from pathlib import Path

st.set_page_config(page_title="RetailPulse Platform", page_icon="⚡", layout="wide")

BASE_DIR = Path(__file__).parent

if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

auth_page = st.Page(BASE_DIR / "pages" / "00_Auth.py", title="Sign In / Sign Up", icon="🔐", default=not st.session_state["authenticated"])

sales_page = st.Page(BASE_DIR / "pages" / "01_Sales_Trends.py", title="Sales & Trends", icon="📈", default=st.session_state["authenticated"])
product_page = st.Page(BASE_DIR / "pages" / "02_Product_Performance.py", title="Product Performance", icon="🏷️")
customer_page = st.Page(BASE_DIR / "pages" / "03_Customer_Analytics.py", title="Customer Analytics", icon="👥")
regional_page = st.Page(BASE_DIR / "pages" / "04_Regional_Sales.py", title="Regional Sales", icon="🌍")
seasonality_page = st.Page(BASE_DIR / "pages" / "05_Seasonality.py", title="Seasonality", icon="📅")
behavior_page = st.Page(BASE_DIR / "pages" / "06_Customer_Behavior.py", title="Customer Behavior", icon="🎯")
profit_page = st.Page(BASE_DIR / "pages" / "07_Profit_And_Revenue.py", title="Profit & Revenue", icon="💰")
inventory_page = st.Page(BASE_DIR / "pages" / "08_Inventory_Risk.py", title="Inventory Risk", icon="📦")
orders_page = st.Page(BASE_DIR / "pages" / "09_Order_Transactions.py", title="Order Transactions", icon="📄")
forecast_page = st.Page(BASE_DIR / "pages" / "10_Demand_Forecasting.py", title="Demand Forecasting", icon="🔮")
filters_page = st.Page(BASE_DIR / "pages" / "11_Interactive_Filters.py", title="Interactive Filters", icon="🎲")

if st.session_state["authenticated"]:
    pg = st.navigation({
        "Account": [auth_page],
        "Analytics Dashboards": [
            sales_page, product_page, customer_page, regional_page, 
            seasonality_page, behavior_page, profit_page, inventory_page, 
            orders_page, forecast_page, filters_page
        ]
    })
else:
    pg = st.navigation({
        "Authentication Required": [auth_page]
    })

pg.run()