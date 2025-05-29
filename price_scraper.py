import requests
import pandas as pd
from datetime import datetime

def get_historical_prices(coin_id, vs_currency='usd', days='90'):
    url = f"https://api.coingecko.com/api/v3/coins/{coin_id}/market_chart"
    params = {
        'vs_currency': vs_currency,
        'days': days,
        'interval': 'daily'
    }

    response = requests.get(url, params=params)
    if response.status_code != 200:
        raise Exception(f"Error fetching data: {response.status_code}")
    
    data = response.json()['prices']
    df = pd.DataFrame(data, columns=["timestamp", "price"])
    df["date"] = pd.to_datetime(df["timestamp"], unit="ms").dt.date
    df = df[["date", "price"]]
    df.columns = ["Date", "Close"]
    return df

if __name__ == "__main__":
    coin_id = "pepe" # Coin ID
    days = 365
    df = get_historical_prices(coin_id, days=days)

    output_path = f"data/{coin_id}_price_data.csv"
    df.to_csv(output_path, index=False)
    print(f"Saved to {output_path}")
    print(df.head())

