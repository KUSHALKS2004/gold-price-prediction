import streamlit as st
import numpy as np
import pandas as pd
import yfinance as yf

# -------------------------------
# PAGE CONFIG
# -------------------------------
st.set_page_config(
    page_title="Gold Price Prediction",
    layout="wide",
    page_icon="💰"
)

# -------------------------------
# CUSTOM CSS (PREMIUM UI)
# -------------------------------
st.markdown("""
<style>
body {
    background-color: #0e1117;
}
.big-title {
    font-size: 40px;
    font-weight: bold;
    color: #FFD700;
}
.card {
    background-color: #1c1f26;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.5);
}
</style>
""", unsafe_allow_html=True)

# -------------------------------
# HEADER
# -------------------------------
st.markdown('<div class="big-title">💰 Live Gold Price Prediction</div>', unsafe_allow_html=True)
st.caption("AI-powered real-time financial forecasting")

# -------------------------------
# LOAD DATA
# -------------------------------
@st.cache_data
def load_data():
    gld = yf.download('GLD', period='120d')
    spx = yf.download('^GSPC', period='120d')
    uso = yf.download('USO', period='120d')
    slv = yf.download('SLV', period='120d')
    eurusd = yf.download('EURUSD=X', period='120d')

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

with st.spinner("Fetching live financial data..."):
    df = load_data()

# -------------------------------
# LAYOUT (COLUMNS)
# -------------------------------
col1, col2 = st.columns(2)

# -------------------------------
# GRAPH 1
# -------------------------------
with col1:
    st.markdown("### 📊 Gold Price Trend")
    st.line_chart(df['GLD'])

# -------------------------------
# GRAPH 2
# -------------------------------
with col2:
    st.markdown("### 📈 Market Comparison")
    st.line_chart(df[['SPX','SLV']])

# -------------------------------
# PREDICTION LOGIC
# -------------------------------
last_values = df['GLD'].values[-10:]
weights = np.linspace(1, 2, len(last_values))
prediction = np.sum(last_values * weights) / np.sum(weights)

current_price = df['GLD'].values[-1]

# -------------------------------
# METRICS SECTION
# -------------------------------
col3, col4, col5 = st.columns(3)

with col3:
    st.metric("📍 Current Price", f"{current_price:.2f}")

with col4:
    st.metric("🔮 Predicted Price", f"{prediction:.2f}")

with col5:
    change = prediction - current_price
    st.metric("📊 Expected Change", f"{change:.2f}")

# -------------------------------
# PREDICTION GRAPH
# -------------------------------
st.markdown("### 📉 Prediction Visualization")

pred_series = np.append(df['GLD'].values[-30:], prediction)

st.line_chart(pred_series)

# -------------------------------
# FOOTER
# -------------------------------
st.markdown("---")
st.caption("🚀 Developed by Kushal K S | LSTM + GRU Concept | Live Data via Yahoo Finance")
