import streamlit as st
import numpy as np
import pandas as pd
import yfinance as yf
from sklearn.preprocessing import MinMaxScaler

st.set_page_config(page_title="Gold Price Prediction", layout="centered")

st.title("💰 Live Gold Price Prediction")
st.write("Fast Deployment Version (Real-Time Data)")

@st.cache_data
def load_data():
    gld = yf.download('GLD', period='90d')
    spx = yf.download('^GSPC', period='90d')
    uso = yf.download('USO', period='90d')
    slv = yf.download('SLV', period='90d')
    eurusd = yf.download('EURUSD=X', period='90d')

    # Combine properly using concat
    df = pd.concat([
        gld['Close'],
        spx['Close'],
        uso['Close'],
        slv['Close'],
        eurusd['Close']
    ], axis=1)

    df.columns = ['GLD', 'SPX', 'USO', 'SLV', 'EUR/USD']

    # Drop missing values
    df.dropna(inplace=True)

    return df

# -------------------------------
# SHOW GRAPH
# -------------------------------
st.subheader("📊 Gold Price Trend")
st.line_chart(df['GLD'])

# -------------------------------
# SIMPLE PREDICTION MODEL (FAST)
# -------------------------------
scaler = MinMaxScaler()
scaled = scaler.fit_transform(df)

# Use last 10 days trend (lightweight prediction)
last_values = df['GLD'].values[-10:]

# Simple weighted prediction
weights = np.linspace(1, 2, len(last_values))
prediction = np.sum(last_values * weights) / np.sum(weights)

# -------------------------------
# DISPLAY RESULT
# -------------------------------
st.metric("💰 Predicted Gold Price", f"{prediction:.2f}")

st.success("✅ Live prediction generated successfully!")

st.caption("Model: Optimized Fast Prediction | Data: Yahoo Finance")
