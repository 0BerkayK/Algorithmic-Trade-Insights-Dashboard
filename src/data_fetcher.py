import requests
import pandas as pd
import os

def fetch_btc_price_data_binance():
    url = "https://api.binance.com/api/v3/klines"
    params = {
        "symbol": "BTCUSDT",
        "interval": "1m",   # 1 minute interval
        "limit": 1440       # 1 day == 1440 minutes
    }
    response = requests.get(url, params=params)
    print("Response status code:", response.status_code)
    data = response.json()

    # data is a list and each element is like this: [open time, open, high, low, close, volume, ...]
    # timestamp (open_time) in ms
    df = pd.DataFrame(data, columns=[
        "open_time", "open", "high", "low", "close", "volume",
        "close_time", "quote_asset_volume", "number_of_trades",
        "taker_buy_base_asset_volume", "taker_buy_quote_asset_volume", "ignore"
    ])

    # Convert timestamp to datetime format
    df["timestamp"] = pd.to_datetime(df["open_time"], unit='ms')

    #
    df = df[["timestamp", "close"]]
    df.rename(columns={"close": "price"}, inplace=True)

    # Path
    if not os.path.exists("data"):
        os.makedirs("data")

    df.to_csv("data/btc_price_data.csv", index=False)
    print("Data saved to 'data/btc_price_data.csv'.")
    return df

if __name__ == "__main__":
    df = fetch_btc_price_data_binance()
    print(df.head())
