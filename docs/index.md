# 🧠 Sentiment-Powered Meme Coin Price Predictor

A machine learning pipeline that analyzes Reddit sentiment to predict price movements of meme coins like $PEPE.

## 📊 Project Overview

This bot:
- Scrapes Reddit posts & comments from multiple crypto subreddits
- Computes sentiment scores using VADER
- Merges this with historical coin price data
- Trains a **regularized linear regression model (Ridge)**
- Outputs **buy/sell/hold signals**
- Backtests the strategy using realistic slippage and transaction cost assumptions

## ⚙️ Project Components

| Component                     | Description                                                                 |
|-------------------------------|-----------------------------------------------------------------------------|
| `reddit_sentiment_scraper.py` | Fetches post and comment sentiment from selected subreddits                 |
| `price_scraper.py`            | Pulls historical price data for the target coin                             |
| `train_model.py`              | Trains a regression model using sentiment and price history                 |
| `signal_generator.py`         | Compares predicted vs actual prices to generate trading signals             |
| `backtest.py`                 | Backtests the strategy using the `bt` Python library                        |
| `data/`                       | Contains cleaned CSVs for sentiment, prices, predictions, and signals       |

## 🧪 Current Performance

- Model: `Ridge Regression`
- Features: Log-transformed price windows + sentiment
- RMSE: (insert your latest value)
- Last test: 2025-05-28
- Plot: <img width="616" alt="Screenshot 2025-05-28 at 5 02 57 PM" src="https://github.com/user-attachments/assets/e1bbbc7c-346d-4c26-a9e3-fe0522239592" />

## 📈 Planned Improvements

### 🎯 Model Enhancements
- [ ] Try LSTM or other time-series models
- [ ] Use transformers or finetuned BERT for deeper sentiment analysis
- [ ] Include **volume** and **price volatility** as additional features

### 💬 Sentiment Enhancements
- [x] Use **multiple subreddits** ✅
- [x] Include **post + body + comments** ✅
- [x] Add **engagement-weighted sentiment** ✅
- [ ] Use **keyword filtering** to exclude spam or off-topic posts
- [ ] Normalize sentiment scores per subreddit to remove subreddit bias

### 🧠 Strategy Logic
- [x] Generate signals based on predicted vs actual ✅
- [x] Add transaction cost thresholds ✅
- [ ] Factor in slippage per coin liquidity
- [ ] Create multi-coin training dataset to generalize model

## 🔁 Backtesting Setup

- Library: [`bt`](https://pmorissette.github.io/bt/)
- Slippage: 0.2%
- Transaction Cost: 0.3%
- Signal logic: BUY if predicted > actual + threshold, SELL if predicted < actual - threshold

## 📚 Research Notes

- VADER is fast & works well for social media, but may not capture sarcasm or hype words effectively
- Most meme coins have very **nonlinear**, hype-driven price action
- Reddit sentiment **lags** real-time price moves slightly
- Future: try real-time trading simulation with a paper-trading API

## ✅ To-Do Tracker

- [ ] Publish cleaned version of the data
- [ ] Compare different time window sizes (e.g. 3 vs 10 vs 20 days)
- [ ] Visualize signal performance over time
- [ ] Build an automated daily retraining script

## ✨ Contributors

- **Jack Polloway** – Creator and full-stack ML engineer on this project

*This project is for fun and educational purposes only. Do not use this as financial advice!*
