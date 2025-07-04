import streamlit as st
import pandas as pd
import plotly.express as px
import datetime
from scipy.stats import zscore


@st.cache_data
def load_data():
    df = pd.read_csv("data/btc_price_data.csv")
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    return df


def main():
    st.set_page_config(page_title="BTC Dashboard", layout="wide")
    st.title("📈 BTC Price Insights Dashboard")

    df = load_data()

    # Time range selector
    st.sidebar.header("📅 Time Range Filter")
    min_time = df["timestamp"].min().to_pydatetime()
    max_time = df["timestamp"].max().to_pydatetime()

    selected_range = st.sidebar.slider(
        "Select time range:",
        min_value=min_time,
        max_value=max_time,
        value=(min_time, max_time),
        format="HH:mm"
    )

    filtered_df = df[(df["timestamp"] >= selected_range[0]) & (df["timestamp"] <= selected_range[1])]

    # --- Technical Indicators ---
    # Convert price to float
    filtered_df["price"] = filtered_df["price"].astype(float)

    # 30-period simple moving average (30 minutes)
    filtered_df["SMA_30"] = filtered_df["price"].rolling(window=30).mean()

    # 30-period volatility (standard deviation)
    filtered_df["Volatility"] = filtered_df["price"].rolling(window=30).std()


    # Statistics
    st.subheader("📊 Price Summary")
    col1, col2, col3 = st.columns(3)
    col1.metric("Minimum Price", f"${filtered_df['price'].astype(float).min():,.2f}")
    col2.metric("Maximum Price", f"${filtered_df['price'].astype(float).max():,.2f}")
    col3.metric("Average Price", f"${filtered_df['price'].astype(float).mean():,.2f}")

    # Price table
    with st.expander("🔍 Raw Data Table"):
        st.dataframe(filtered_df.tail(10), use_container_width=True)

    # Graph
    st.subheader("📈 BTC Price Over Time")
    fig = px.line(filtered_df, x="timestamp", y="price", title="BTC Price (USD)",
                  labels={"price": "Price (USD)", "timestamp": "Timestamp"})
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("📈 BTC Price with Moving Average")

    fig = px.line(filtered_df, x="timestamp", y=["price", "SMA_30"],
                  labels={"value": "Price (USD)", "timestamp": "Time", "variable": "Metric"},
                  title="BTC Price & SMA (30-min)")

    st.plotly_chart(fig, use_container_width=True)

    # Volatility chart
    st.subheader("📉 Price Volatility (30-min Rolling Std)")

    fig2 = px.line(filtered_df, x="timestamp", y="Volatility",
                   labels={"Volatility": "Standard Deviation", "timestamp": "Time"},
                   title="BTC Price Volatility")

    st.plotly_chart(fig2, use_container_width=True)

    # Anomaly detection with Z-score
    filtered_df["z_score"] = zscore(filtered_df["price"].fillna(method="ffill"))

    # Mark those with |z| > 2.5 as anomalies
    filtered_df["anomaly"] = filtered_df["z_score"].abs() > 2.5

    st.subheader("🚨 Price Anomalies")

    anomaly_df = filtered_df[filtered_df["anomaly"] == True]

    fig3 = px.line(filtered_df, x="timestamp", y="price", title="BTC Price with Anomalies")
    fig3.add_scatter(x=anomaly_df["timestamp"], y=anomaly_df["price"],
                     mode='markers', name='Anomalies',
                     marker=dict(color='red', size=6, symbol='x'))

    st.plotly_chart(fig3, use_container_width=True)

    # SMA crossover
    filtered_df["signal"] = "HOLD"
    filtered_df.loc[filtered_df["price"] < filtered_df["SMA_30"], "signal"] = "BUY"
    filtered_df.loc[filtered_df["price"] > filtered_df["SMA_30"], "signal"] = "SELL"

    st.subheader("📌 Buy / Sell Signals")

    buy_signals = filtered_df[filtered_df["signal"] == "BUY"]
    sell_signals = filtered_df[filtered_df["signal"] == "SELL"]

    fig4 = px.line(filtered_df, x="timestamp", y="price", title="Buy/Sell Signals on Price")

    fig4.add_scatter(x=buy_signals["timestamp"], y=buy_signals["price"],
                     mode="markers", name="BUY", marker=dict(color="green", size=6, symbol="triangle-up"))

    fig4.add_scatter(x=sell_signals["timestamp"], y=sell_signals["price"],
                     mode="markers", name="SELL", marker=dict(color="red", size=6, symbol="triangle-down"))

    st.plotly_chart(fig4, use_container_width=True)

    st.subheader("📋 Last 10 Buy/Sell Signals")
    signal_df = filtered_df[filtered_df["signal"].isin(["BUY", "SELL"])]
    st.dataframe(signal_df[["timestamp", "price", "signal"]].tail(10), use_container_width=True)


if __name__ == "__main__":
    main()
