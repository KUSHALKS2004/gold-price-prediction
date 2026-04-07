import streamlit as st
import numpy as np
import pandas as pd
import yfinance as yf
from tensorflow.keras.models import load_model
from sklearn.preprocessing import MinMaxScaler

st.set_page_config(page_title="Gold Price Prediction", layout="centered")

st.title("💰 Live Gold Price Prediction (LSTM + GRU)")
st.write("Using real-time financial data")

# Load model
model = load_model("gold_lstm_gru.h5")

# Fetch live data
@st.cache_data
def load_data():
    gld = yf.download('GLD', period='90d')
    spx = yf.download('^GSPC', period='90d')
    uso = yf.download('USO', period='90d')
    slv = yf.download('SLV', period='90d')
    eurusd = yf.download('EURUSD=X', period='90d')

    df = pd.DataFrame({
        'GLD': gld['Close'],
        'SPX': spx['Close'],
        'USO': uso['Close'],
        'SLV': slv['Close'],
        'EUR/USD': eurusd['Close']
    })

    df.dropna(inplace=True)
    return df

df = load_data()

st.subheader("📊 Latest Data")
st.line_chart(df['GLD'])

# Scaling
scaler = MinMaxScaler()
scaled = scaler.fit_transform(df)

# Prepare input
last_60 = scaled[-60:]
last_60 = np.reshape(last_60, (1, 60, scaled.shape[1]))

# Predict
prediction = model.predict(last_60)

dummy = np.zeros((1, scaled.shape[1]))
dummy[0,0] = prediction

price = scaler.inverse_transform(dummy)[0,0]

st.success(f"💰 Predicted Gold Price: {price:.2f}")

st.caption("Model: LSTM + GRU | Data: Yahoo Finance")
