# 🧠 Algorithmic Trading Bot (Road to Quant)

A modular, event-driven trading system.

## 🚀 Current Features
- Collects Reddit post + comment sentiment from multiple crypto subreddits
- Combines with historical price data for feature generation
- Ridge regression model predicts log-transformed price
- Generates Buy / Sell / Hold signals
- Backtests the strategy using realistic trading costs

## 📁 Key Files
- `reddit_sentiment_scraper.py`: Reddit sentiment extractor
- `price_scraper.py`: Coin price history
- `merge_sentiment_price.py`: Data joiner
- `train_model.py`: Machine learning model
- `signal_generator.py`: Signal labeling
- `backtest.py`: Backtesting with slippage and transaction costs

## 📚 Quick Links

- See detailed archetecture plans, research, and improvements: [Detailed Documentation](./docs/index.md))
- See detailed my personal notes and thoughts throughout the project: [Logbook](./docs/logbook.md))
- See detailed roadmaps and task tracking details: [Project Management Tracking](./docs/pm.md))

## ⚠️ Disclaimer
This project is purely for research purposes and is **not financial advice**!