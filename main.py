from src.data_fetcher import fetch_btc_price_data_binance

def main():
    print("Fetching BTC price data from Binance API...")
    df = fetch_btc_price_data_binance()
    print("First 5 records:")
    print(df.head())

if __name__ == "__main__":
    main()
