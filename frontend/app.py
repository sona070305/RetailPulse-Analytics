# Pass repository-root relative paths
auth_page = st.Page(
    "frontend/pages/00_Auth.py",
    title="Sign In / Sign Up",
    icon="🔐",
    default=not st.session_state["authenticated"],
)
sales_page = st.Page(
    "frontend/pages/01_Sales_Trends.py",
    title="Sales & Trends",
    icon="📈",
    default=st.session_state["authenticated"],
)
customer_page = st.Page(
    "frontend/pages/02_Customer_Analytics.py",
    title="Customer Analytics",
    icon="👥",
)
forecast_page = st.Page(
    "frontend/pages/03_Demand_Forecasting.py",
    title="Demand Forecasting",
    icon="🔮",
)