import streamlit as st

st.set_page_config(page_title="RetailPulse Platform", page_icon="⚡", layout="wide")

# Initialize global authentication state
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

# Define Pages
auth_page = st.Page("pages/00_Auth.py", title="Sign In / Sign Up", icon="🔐", default=not st.session_state["authenticated"])
sales_page = st.Page("pages/01_Sales_Trends.py", title="Sales & Trends", icon="📈", default=st.session_state["authenticated"])
customer_page = st.Page("pages/02_Customer_Analytics.py", title="Customer Analytics", icon="👥")
forecast_page = st.Page("pages/03_Demand_Forecasting.py", title="Demand Forecasting", icon="🔮")

# Access Control Navigation
if st.session_state["authenticated"]:
    pg = st.navigation({
        "Account": [auth_page],
        "Analytics Dashboards": [sales_page, customer_page, forecast_page]
    })
else:
    pg = st.navigation({
        "Authentication Required": [auth_page]
    })

# Render Active Page
pg.run()