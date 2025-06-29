---
# 📈 Meme Coin Price Predictor (Documentation)
---

Welcome to the full documentation and research journal of the **Meme Coin Price Predictor**, a project built to forecast meme coin price directionality (BUY / SELL signals) based on Reddit sentiment analysis and historical price data.

---

## 🧠 Project Overview
This bot collects sentiment signals from crypto subreddits and combines them with price history to make predictions using a Ridge regression model. It then generates trading signals and backtests the strategy using realistic market conditions.

---

## 🧱 Current Architecture Overview

```
Reddit Posts+Comments               Price Data (API)           
         │                                 │
         ▼                                 ▼
Sentiment Analyzer                 Historical Price CSV
         │                                 │
         └─────► Merge & Align Dates ◄─────┘
                         │
                         ▼
       Feature Construction (log price + sentiment window)
                         │
                         ▼
                Ridge Regression Training
                         │
                         ▼
            Prediction + Signal Generation
                         │
                         ▼
              Backtesting + Performance
```

---

## 🧪 Current Performance

- Model: `Ridge Regression`
- Features: Log-transformed price windows + sentiment
- RMSE: (insert latest value)
- Last test: 28-05-2025
- Plot: ![Prediction Graph](./assets%20/model_performance.png)

---

## 🔍 Research & Improvements

### Ideal Archetecture (What You Need for a Cracked Bot):

1. Signal Generation (Alpha):
Already using sentiment and price trends, Add:
- Fourier/Seasonality Decomposition: Extract cyclical components from price series.
- Regime Detection: Use HMMs or clustering to detect market states.
    - [Interresting resource](https://medium.com/@tballz/regime-detection-and-prediction-in-financial-markets-lesson-1-simple-tutorial-42ee5bf18d61)
- Feature Engineering: 
    - Momentum, RSI, MACD.
    - Sentiment momentum (rate of sentiment change).
    - Volatility, drawdowns, unusual volume spikes.

2. Volatility Modeling:
For risk-aware strategies and sizing.
- GARCH models (e.g., arch library): Predict volatility
- Neural Networks:
    - LSTM for volatility forcasting.
    - Or simple feedforward networks using lagged volatility, volume, sentiment as input data.

3. Position Sizing / Portfolio Optimization:
Add:
- Kelly Criterion: Optimal fractional betting size.
- Mean-Varience Optimization (Markowitz).
- Convex optimization with constraings (e.g., maximum exposure, minimum cash).
- Risk-parity weighting.

4. Backtesting Engine:
Already using `bt`, also explore:
- `backtrader` for better flexability.
- `quantconnect` (cloud).
Add features like: 
- Slippage modeling.
- Market impace (advanced).
- Multi-asset testing.

5. Execution Engine (Optional for now?):
If you want to simulate real trading. IDK how this is different for backtest - will look into it later.

### ✅ Done:
- Multi-subreddit sentiment scraping
- VADER for sentiment analysis
- Combined title + body + comment sentiment
- Engagement-weighted scoring (based on post score)
- Time window features (past 100 days)
- Log transformation of prices
- Signal generation (BUY/SELL/HOLD)
- Transaction cost and slippage modeling

### 🧪 In Progress / To Do:
- [ ] Basic backtesting using `bt`
- [ ] Add visualizations to GitHub Pages (charts, RMSE trends)
- [ ] Compare Ridge vs. other models (e.g., Random Forest, LSTM)
- [ ] Weight by subreddit influence / credibility
- [ ] Use Reddit comment trees to weight replies more carefully
- [ ] Add support for Twitter / Discord scraping
- [ ] Try reinforcement learning for trading strategy
- [ ] Export prediction dashboard (e.g. Streamlit app)

---

## 📁 File Structure
- `reddit_sentiment_scraper.py`: Collects and scores Reddit posts
- `price_scraper.py`: Downloads and formats historical coin prices
- `merge_sentiment_price.py`: Combines data sources
- `train_model.py`: Builds and trains Ridge regression model
- `signal_generator.py`: Generates Buy / Sell signals
- `backtest.py`: Runs backtest using `bt`

---

## 📊 Backtesting Setup
- Uses `bt` library to evaluate signal strategy
- Assumes 0.5% transaction cost and 0.2% slippage
- Equity curve and performance metrics output in terminal (and can be extended)

---

## ⚠️ Disclaimer
This project is purely for research purposes and is **not financial advice**!

Feel free to fork or adapt this bot to explore crypto-sentiment-based investing!
