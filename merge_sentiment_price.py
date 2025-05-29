import pandas as pd

sentiment_df = pd.read_csv("data/reddit_sentiment_pepe.csv")
price_df = pd.read_csv("data/pepe_price_data.csv")

# Group sentiment by date
daily_sentiment = sentiment_df.groupby("Date")["Sentiment"].mean().reset_index()
daily_sentiment.columns = ["Date", "Avg_Sentiment"]

merged_df = pd.merge(price_df, daily_sentiment, on="Date", how="inner")

merged_df.to_csv("data/pepe_merged_data.csv", index=False)

print("Merged pepe sentiment and price data")
print(merged_df.head())