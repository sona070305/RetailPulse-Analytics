import streamlit as st

st.set_page_config(page_title="Auth Portal | RetailPulse", page_icon="⚡", layout="wide")

# --- Custom CSS for Colorful & Animated UI ---
st.markdown("""
<style>
/* Animated Gradient Background */
@keyframes gradientBG {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

/* Floating Card Animation */
@keyframes float {
    0% { transform: translateY(0px); }
    50% { transform: translateY(-10px); }
    100% { transform: translateY(0px); }
}

/* Glow Pulse Animation */
@keyframes pulseGlow {
    0% { box-shadow: 0 0 15px rgba(124, 58, 237, 0.4); }
    50% { box-shadow: 0 0 35px rgba(236, 72, 153, 0.7); }
    100% { box-shadow: 0 0 15px rgba(124, 58, 237, 0.4); }
}

/* Hero Title Styling */
.hero-title {
    font-size: 3rem;
    font-weight: 800;
    background: linear-gradient(135deg, #FF007A, #7B2CBF, #00F5D4);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    text-align: center;
    margin-bottom: 5px;
    animation: float 4s ease-in-out infinite;
}

.hero-subtitle {
    text-align: center;
    color: #A0AEC0;
    font-size: 1.1rem;
    margin-bottom: 25px;
}

/* Glassmorphism Auth Container */
.auth-card {
    background: rgba(23, 25, 35, 0.75);
    backdrop-filter: blur(16px);
    border: 1px solid rgba(255, 255, 255, 0.12);
    border-radius: 20px;
    padding: 30px;
    animation: pulseGlow 6s infinite alternate;
}
</style>
""", unsafe_allow_html=True)

# --- Hero Header ---
st.markdown('<div class="hero-title">⚡ RetailPulse Portal</div>', unsafe_allow_html=True)
st.markdown('<div class="hero-subtitle">AI-Powered Analytics & Customer Intelligence Engine</div>', unsafe_allow_html=True)

# Initialize global user database & session state
if "users_db" not in st.session_state:
    st.session_state["users_db"] = {
        "admin": "admin123",
        "bhargav": "retailpulse2026"
    }

if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

# Center Auth Box
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    if st.session_state["authenticated"]:
        st.balloons()
        st.success(f"🎉 Welcome back, **{st.session_state.get('username', 'User')}**!")
        st.info("🔓 All analytics dashboards are unlocked in the sidebar navigation.")
        if st.button("🚪 Log Out", type="primary", use_container_width=True):
            st.session_state["authenticated"] = False
            st.session_state["username"] = None
            st.rerun()
    else:
        tab1, tab2 = st.tabs(["🚀 Sign In", "✨ Create Account"])

        with tab1:
            st.markdown("### 🔑 Welcome Back")
            username = st.text_input("Username", key="signin_user", placeholder="Enter your username")
            password = st.text_input("Password", type="password", key="signin_pass", placeholder="••••••••")
            
            if st.button("Sign In to Platform", type="primary", use_container_width=True):
                users = st.session_state["users_db"]
                if username in users and users[username] == password:
                    st.session_state["authenticated"] = True
                    st.session_state["username"] = username
                    st.toast("Authentication Successful!", icon="🎉")
                    st.rerun()
                else:
                    st.error("Invalid username or password.")

        with tab2:
            st.markdown("### 📝 Join RetailPulse")
            new_user = st.text_input("Choose Username", key="signup_user", placeholder="e.g., alex_data")
            new_pass = st.text_input("Choose Password", type="password", key="signup_pass", placeholder="••••••••")
            confirm_pass = st.text_input("Confirm Password", type="password", key="confirm_pass", placeholder="••••••••")
            
            if st.button("Register Account", use_container_width=True):
                if not new_user or not new_pass:
                    st.error("Please fill in all details.")
                elif new_user in st.session_state["users_db"]:
                    st.warning("Username already registered.")
                elif new_pass != confirm_pass:
                    st.error("Passwords do not match.")
                else:
                    st.session_state["users_db"][new_user] = new_pass
                    st.success("Account created successfully! Click on 'Sign In' to enter.")