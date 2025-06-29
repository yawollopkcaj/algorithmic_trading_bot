# 🧠 Meme Coin Price Predictor

A machine learning-based crypto trading bot that predicts meme coin price movements using Reddit sentiment and historical price data.

## 🚀 Features
- Collects Reddit post + comment sentiment from multiple crypto subreddits
- Combines with historical price data for feature generation
- Ridge regression model predicts log-transformed price
- Generates Buy / Sell / Hold signals
- Backtests the strategy using realistic trading costs

## 📊 Signal Logic
If the model predicts the price will increase compared to current value: **BUY**.  
If it predicts a decrease: **SELL**.  
Otherwise: **HOLD**.

## 📁 Key Files
- `reddit_sentiment_scraper.py`: Reddit sentiment extractor
- `price_scraper.py`: Coin price history
- `merge_sentiment_price.py`: Data joiner
- `train_model.py`: Machine learning model
- `signal_generator.py`: Signal labeling
- `backtest.py`: Backtesting with slippage and transaction costs

## 📚 Full Documentation
See detailed architecture, research plans, and improvements on the [GitHub Pages site](https://yawollopkcaj.github.io/price-predictor/docs/index.md)

## ⚠️ Disclaimer
This is a research project only. **Not financial advice!**
