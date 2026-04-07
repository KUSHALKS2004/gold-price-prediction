import streamlit as st
import numpy as np
import pandas as pd
import yfinance as yf

# -------------------------------
# PAGE CONFIG
# -------------------------------
st.set_page_config(page_title="Gold AI Dashboard", layout="wide", page_icon="💰")

# -------------------------------
# SIMPLE LOGIN SYSTEM
# -------------------------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

def login():
    st.title("🔐 Login to Gold Prediction Dashboard")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username == "admin" and password == "1234":
            st.session_state.logged_in = True
        else:
            st.error("Invalid Credentials")

if not st.session_state.logged_in:
    login()
    st.stop()

# -------------------------------
# PREMIUM UI CSS
# -------------------------------
st.markdown("""
<style>
body {
    background: linear-gradient(to right, #0f2027, #203a43, #2c5364);
}
.card {
    background: rgba(255,255,255,0.05);
    padding: 20px;
    border-radius: 15px;
    backdrop-filter: blur(10px);
}
.big-title {
    font-size: 42px;
    font-weight: bold;
    color: gold;
}
</style>
""", unsafe_allow_html=True)

# -------------------------------
# HEADER
# -------------------------------
st.markdown('<div class="big-title">💰 AI Gold Price Dashboard</div>', unsafe_allow_html=True)
st.caption("Advanced Predictive Analytics using Live Financial Data")

# -------------------------------
# LOAD DATA
# -------------------------------
@st.cache_data
def load_data():
    gld = yf.download('GLD', period='150d')
    spx = yf.download('^GSPC', period='150d')
    uso = yf.download('USO', period='150d')
    slv = yf.download('SLV', period='150d')
    eurusd = yf.download('EURUSD=X', period='150d')

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

with st.spinner("Loading live market data..."):
    df = load_data()

# -------------------------------
# SIDEBAR CONTROLS
# -------------------------------
st.sidebar.title("⚙️ Settings")

days = st.sidebar.slider("Select Days", 30, 150, 60)

# -------------------------------
# MAIN DASHBOARD
# -------------------------------
col1, col2 = st.columns(2)

with col1:
    st.subheader("📊 Gold Price Trend")
    st.line_chart(df['GLD'].tail(days))

with col2:
    st.subheader("📈 Market Indicators")
    st.line_chart(df[['SPX','SLV']].tail(days))

# -------------------------------
# PREDICTION LOGIC
# -------------------------------
last_values = df['GLD'].values[-10:]
weights = np.linspace(1, 2, len(last_values))
prediction = np.sum(last_values * weights) / np.sum(weights)

current_price = df['GLD'].values[-1]
change = prediction - current_price

# -------------------------------
# METRICS
# -------------------------------
c1, c2, c3 = st.columns(3)

c1.metric("📍 Current Price", f"{current_price:.2f}")
c2.metric("🔮 Predicted Price", f"{prediction:.2f}")
c3.metric("📊 Expected Change", f"{change:.2f}")

# -------------------------------
# AI EXPLANATION
# -------------------------------
st.markdown("### 🤖 AI Insight")

if change > 0:
    st.success("Gold price is expected to rise based on recent upward trends and market signals.")
else:
    st.warning("Gold price may decline slightly due to recent downward trends.")

# -------------------------------
# PREDICTION GRAPH
# -------------------------------
st.markdown("### 📉 Prediction Visualization")

pred_series = np.append(df['GLD'].values[-30:], prediction)
st.line_chart(pred_series)

# -------------------------------
# DOWNLOAD REPORT
# -------------------------------
st.markdown("### 📥 Download Report")

report = df.tail(days).to_csv().encode('utf-8')

st.download_button(
    label="Download Data Report",
    data=report,
    file_name="gold_price_report.csv",
    mime='text/csv'
)

# -------------------------------
# FOOTER
# -------------------------------
st.markdown("---")
st.caption("🚀 Developed by Kushal K S | AI Gold Prediction System")
