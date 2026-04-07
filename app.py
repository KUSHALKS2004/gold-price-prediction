import streamlit as st
import numpy as np
import pandas as pd
import yfinance as yf
import time

# -------------------------------
# PAGE CONFIG
# -------------------------------
st.set_page_config(page_title="Gold AI Pro", layout="wide", page_icon="💰")

# -------------------------------
# SESSION LOGIN STATE
# -------------------------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# -------------------------------
# LOGIN PAGE (ENHANCED)
# -------------------------------
def login():
    st.markdown("<h1 style='text-align:center;color:gold;'>🔐 Gold AI Login</h1>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1,2,1])

    with col2:
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if st.button("Login"):
            if username == "admin" and password == "1234":
                st.success("Login Successful!")
                time.sleep(1)
                st.session_state.logged_in = True
                st.rerun()
            else:
                st.error("Invalid Credentials")

if not st.session_state.logged_in:
    login()
    st.stop()

# -------------------------------
# PREMIUM CSS + ANIMATION
# -------------------------------
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
}
.title {
    font-size: 45px;
    font-weight: bold;
    color: gold;
    animation: fadeIn 2s ease-in;
}
@keyframes fadeIn {
    from {opacity:0;}
    to {opacity:1;}
}
.card {
    background: rgba(255,255,255,0.05);
    padding: 20px;
    border-radius: 15px;
    backdrop-filter: blur(10px);
}
</style>
""", unsafe_allow_html=True)

# -------------------------------
# HEADER
# -------------------------------
st.markdown("<div class='title'>💰 Gold AI Prediction Dashboard</div>", unsafe_allow_html=True)
st.caption("Real-Time Intelligent Financial Forecasting System")

# -------------------------------
# LOAD DATA (OPTIMIZED)
# -------------------------------
@st.cache_data(ttl=3600)
def load_data():
    gld = yf.download('GLD', period='180d')
    spx = yf.download('^GSPC', period='180d')
    uso = yf.download('USO', period='180d')
    slv = yf.download('SLV', period='180d')
    eurusd = yf.download('EURUSD=X', period='180d')

    df = pd.concat([
        gld['Close'],
        spx['Close'],
        uso['Close'],
        slv['Close'],
        eurusd['Close']
    ], axis=1)

    df.columns = ['GLD', 'SPX', 'USO', 'SLV', 'EUR/USD']
    df.dropna(inplace=True)

    return df

with st.spinner("📡 Fetching live market data..."):
    df = load_data()

# -------------------------------
# SIDEBAR (SMART CONTROL)
# -------------------------------
st.sidebar.title("⚙️ Dashboard Controls")

days = st.sidebar.slider("Select Time Range (Days)", 30, 180, 90)
show_data = st.sidebar.checkbox("Show Raw Data")

# -------------------------------
# MAIN DASHBOARD
# -------------------------------
col1, col2 = st.columns(2)

with col1:
    st.subheader("📊 Gold Price Trend")
    st.line_chart(df['GLD'].tail(days))

with col2:
    st.subheader("📈 Market Comparison")
    st.line_chart(df[['SPX','SLV']].tail(days))

# -------------------------------
# PREDICTION LOGIC (ENHANCED)
# -------------------------------
last_values = df['GLD'].values[-15:]

weights = np.linspace(1, 3, len(last_values))
prediction = np.sum(last_values * weights) / np.sum(weights)

current_price = df['GLD'].values[-1]
change = prediction - current_price
percentage = (change / current_price) * 100

# -------------------------------
# METRICS (ANIMATED STYLE)
# -------------------------------
c1, c2, c3 = st.columns(3)

c1.metric("📍 Current Price", f"{current_price:.2f}")
c2.metric("🔮 Predicted Price", f"{prediction:.2f}")
c3.metric("📊 Change (%)", f"{percentage:.2f}%")

# -------------------------------
# AI INSIGHT (SMART TEXT)
# -------------------------------
st.markdown("### 🤖 AI Market Insight")

if percentage > 1:
    st.success("📈 Strong upward trend detected. Market indicators suggest bullish momentum.")
elif percentage > 0:
    st.info("🔼 Slight increase expected. Market is stable with mild growth.")
elif percentage < -1:
    st.error("📉 Downward pressure observed. Possible bearish trend ahead.")
else:
    st.warning("⚖️ Market is stable with minimal fluctuations.")

# -------------------------------
# PREDICTION VISUAL
# -------------------------------
st.markdown("### 📉 Prediction Visualization")

pred_series = np.append(df['GLD'].values[-40:], prediction)
st.line_chart(pred_series)

# -------------------------------
# OPTIONAL DATA VIEW
# -------------------------------
if show_data:
    st.markdown("### 📄 Raw Data")
    st.dataframe(df.tail(days))

# -------------------------------
# DOWNLOAD REPORT
# -------------------------------
st.markdown("### 📥 Export Data")

csv = df.tail(days).to_csv().encode('utf-8')

st.download_button(
    label="Download CSV Report",
    data=csv,
    file_name="gold_ai_report.csv",
    mime='text/csv'
)

# -------------------------------
# FOOTER (BRANDING)
# -------------------------------
st.markdown("---")
st.caption("🚀 Developed by Kushal K S | AI Gold Prediction System | 2026")
