# 💰 Gold Price Prediction System

🚀 An AI-powered web application that predicts gold prices using real-time financial data and advanced time-series techniques.

---

## 🌐 Live Demo

👉 https://gold-price-prediction-nh3q9mcq7cpea4enddtvvp.streamlit.app/

---

## 📌 Project Overview

This project predicts gold prices using historical and live financial market data.  
It integrates deep learning techniques for training and a lightweight model for real-time deployment.

The system is deployed as an interactive web dashboard using Streamlit.

---

## 🎯 Key Features

✔ Real-time gold price visualization  
✔ Live prediction system  
✔ Market comparison (SPX, SLV, etc.)  
✔ AI-based insights  
✔ Secure login system  
✔ Downloadable reports  
✔ Interactive dashboard UI  

---

## 🧠 Models Used

### 🔹 Training Phase (Google Colab)
- LSTM (Long Short-Term Memory)
- GRU (Gated Recurrent Unit)

👉 Used for capturing time-series patterns and improving prediction accuracy.

---

### 🔹 Deployment Phase (Streamlit App)
- Weighted Moving Average (Lightweight Model)

👉 Used for fast real-time predictions due to cloud limitations.

---

## ⚙️ Tech Stack

- Python  
- Streamlit  
- Pandas  
- NumPy  
- Scikit-learn  
- TensorFlow (training phase)  
- yFinance API (live data)

---

## 📊 System Architecture
Data Source (yFinance)
↓
Data Preprocessing
↓
LSTM + GRU Model (Training)
↓
Prediction Logic
↓
Streamlit Web Application
↓
User Dashboard


---

## 📁 Project Structure
gold-price-prediction/
│
├── app.py # Main Streamlit app
├── requirements.txt # Dependencies
├── README.md # Documentation


---

## 🚀 Installation & Setup

### 1️⃣ Clone Repository
git clone https://github.com/KUSHALKS2004/gold-price-prediction.git

cd gold-price-prediction


---

### 2️⃣ Install Dependencies
pip install -r requirements.txt


---

### 3️⃣ Run App
streamlit run app.py


---

## 🔐 Login Credentials
Username: admin
Password: 1234


---

## 📈 How It Works

1. Fetches live financial data using yFinance  
2. Processes and aligns market indicators  
3. Applies prediction logic  
4. Displays results in an interactive dashboard  

---

## 📊 Output

- 📈 Gold price trend graph  
- 🔮 Predicted price  
- 📊 Market comparison  
- 🤖 AI insights  

---

## 🎓 Academic Value

This project demonstrates:

- Time-series forecasting  
- Deep learning models (LSTM & GRU)  
- Real-time data integration  
- Web app deployment  

---

## ⚠️ Limitations

- Lightweight model used in deployment  
- Prediction accuracy depends on data quality  
- Market volatility affects results  

---

## 🔮 Future Enhancements

- Deploy full LSTM model via API  
- Add database authentication  
- Improve prediction accuracy  
- Mobile application support  

---

## 👨‍💻 Author

**Kushal K S**

---

## 📜 License

This project is for educational purposes only.
