# 📈 Algorithmic Trade Insights – BTC Price Analytics Dashboard

**Simulating a real-world data science workflow for an algorithmic trading environment.**  
This project was developed as part of a self-initiated case study inspired by the job description at BlockTech. It demonstrates my end-to-end capabilities in collecting real-time financial data, analyzing it using statistical and technical indicators, and building an interactive visualization platform for traders and analysts.

---

## 🎯 Project Objective

To build a complete data science pipeline that:

- Retrieves high-frequency Bitcoin price data
- Performs time-series analysis and anomaly detection
- Generates trading signals using SMA crossover
- Visualizes everything in an interactive dashboard for actionable insights

---


---

## 🔧 Technologies Used

| Purpose               | Tools / Libraries                  |
|------------------------|-----------------------------------|
| Data Collection        | `requests`, `Binance API`         |
| Data Manipulation      | `pandas`, `numpy`                 |
| Statistical Analysis   | `scipy` (Z-score)                 |
| Technical Indicators   | `rolling mean`, `std deviation`   |
| Visualization          | `plotly.express`, `streamlit`     |

---

## 🚀 Features

- ✅ Real-time price data fetching from Binance (1-min interval)
- ✅ Data saved as CSV for reproducibility
- ✅ SMA (Simple Moving Average) and Volatility analysis
- ✅ Z-score based anomaly detection
- ✅ Buy/Sell signal generation using SMA crossover logic
- ✅ Fully interactive dashboard with sliders and filters

---

## 📊 Dashboard Preview
 
![Dashboard Preview](dashboard/assets/BTC_Price_Over_Time.png)

![Dashboard Preview](dashboard/assets/BTC_Price_Moving_Average.png)

![Dashboard Preview](dashboard/assets/Price_Volatility.png)

![Dashboard Preview](dashboard/assets/Price_Anomalies.png)

![Dashboard Preview](dashboard/assets/Buy&Sell_Signals.png)

![Dashboard Preview](dashboard/assets/Last_10_Buy&Sell_Signals.png)



---

## 🔍 Step-by-Step Breakdown

### ✅ Step 1 – Project Setup
- Created the folder structure: `src/`, `data/`, `dashboard/`
- Installed required libraries via `pip`

---

### ✅ Step 2 – Data Collection
- Connected to the [Binance API](https://api.binance.com)
- Pulled 1-day worth of BTC/USDT price data at 1-minute intervals
- Parsed and saved as `data/btc_price_data.csv`

---

### ✅ Step 3 – Data Fetcher Script
- Wrote `data_fetcher.py` to handle the API call
- Converted Unix timestamps into `datetime`
- Exported clean CSV ready for analysis

---

### ✅ Step 4 – Streamlit App Setup
- Created `app.py` inside the `dashboard/` folder
- Loaded and displayed the raw data
- Visualized basic price trend using `plotly.express`

---

### ✅ Step 5 – Interactive Controls
- Added a sidebar time-range slider
- Enabled users to filter the graph dynamically
- Refreshed table and visuals based on selected time

---

### ✅ Step 6 – Technical Indicators
- Calculated 30-point Simple Moving Average (SMA)
- Calculated Rolling Volatility using standard deviation
- Visualized both on time-series graphs

---

### ✅ Step 7 – Anomaly Detection
- Applied Z-Score on price data
- Marked anomalies when z > 2.5 or z < -2.5
- Visualized anomalies on the price chart

---

### ✅ Step 8 – Signal Generation
- Created a simple SMA crossover strategy:
    - Price > SMA → **SELL**
    - Price < SMA → **BUY**
- Highlighted buy/sell signals on the graph
- Added a table to show last 10 signals

---

## 📁 How to Run

1. Clone the repo  
2. Install requirements  
```bash
pip install -r requirements.txt

---

## 📐 Technical & Statistical Concepts

This section documents the formulas and concepts used in this project.

---

### 📊 Simple Moving Average (SMA)

SMA is used to smooth out price data by averaging a number of past prices.

**Formula:**

\[
SMA_t = \frac{1}{n} \sum_{i=0}^{n-1} P_{t-i}
\]

- \( P_t \): Price at time \( t \)
- \( n \): Number of periods (e.g., 30 minutes)

In this project, we used **30-period SMA** to track short-term price trends.

---

### 📈 Rolling Volatility (Standard Deviation)

Volatility measures the amount of variation or dispersion of a set of price values.

**Formula:**

\[
\sigma_t = \sqrt{ \frac{1}{n} \sum_{i=0}^{n-1} (P_{t-i} - \mu)^2 }
\]

- \( \mu \): Mean price over the period
- \( \sigma_t \): Rolling standard deviation at time \( t \)

This helps us understand how "noisy" or stable the market is at a given time.

---

### 🚨 Z-Score Based Anomaly Detection

Z-score tells us how far a price is from the mean in terms of standard deviations.

**Formula:**

\[
z_t = \frac{P_t - \mu}{\sigma}
\]

- If \( |z| > 2.5 \), the price is considered an **anomaly**.

In our dashboard, anomalies are visualized as red "X" markers on the price chart.

---

### 📉 SMA Crossover Trading Strategy

A basic buy/sell logic using price and moving average:

- If \( P_t < SMA_t \): **BUY signal**
- If \( P_t > SMA_t \): **SELL signal**

This is a simple but effective strategy to follow momentum reversals.

---


