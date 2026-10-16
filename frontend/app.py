import streamlit as st

st.set_page_config(page_title="RetailPulse Platform", page_icon="⚡", layout="wide")

# Initialize global authentication state
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

# Define Pages with exact filenames and emojis from your pages/ folder
auth_page = st.Page("pages/00_Auth.py", title="Sign In / Sign Up", icon="🔐", default=not st.session_state["authenticated"])

sales_page = st.Page("pages/01_📈_Sales_Trends.py", title="Sales & Trends", icon="📈", default=st.session_state["authenticated"])
product_page = st.Page("pages/02_🏷️_Product_Performance.py", title="Product Performance", icon="🏷️")
customer_page = st.Page("pages/03_👥_Customer_Analytics.py", title="Customer Analytics", icon="👥")
regional_page = st.Page("pages/04_🌍_Regional_Sales.py", title="Regional Sales", icon="🌍")
seasonality_page = st.Page("pages/05_📅_Seasonality.py", title="Seasonality", icon="📅")
behavior_page = st.Page("pages/06_🎯_Customer_Behavior.py", title="Customer Behavior", icon="🎯")
profit_page = st.Page("pages/07_💰_Profit_And_Revenue.py", title="Profit & Revenue", icon="💰")
inventory_page = st.Page("pages/08_📦_Inventory_Risk.py", title="Inventory Risk", icon="📦")
orders_page = st.Page("pages/09_📄_Order_Transactions.py", title="Order Transactions", icon="📄")
forecast_page = st.Page("pages/10_🔮_Demand_Forecasting.py", title="Demand Forecasting", icon="🔮")
filters_page = st.Page("pages/11_🎲_Interactive_Filters.py", title="Interactive Filters", icon="🎲")

# Access Control Navigation
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

# Render Active Page
pg.run()