# Sentiment-Powered Crypto Price Predictor

This project predicts short-term price movements of meme coins using Reddit sentiment and price data.

## 🔧 Components
- 'reddit_sentiment_scraper.py': Scrapes Reddit posts and analyzes sentiment
- 'price_scraper.py': Pulls historical coin prices from CoinGeko
- 'train_model.py': Trains a Ridge Redression model on price + sentiment
- 'signal_generator.py': Generates BUY/SELL signals
- 'backtest.py': Evaluates the performance with backtesting

## 🚀 Getting Started
```bash
pip install -r requirements.txt
python reddit_sentiment_scraper.py
python price_scraper.py
python train_model.py

