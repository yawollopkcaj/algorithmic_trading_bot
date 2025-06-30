---
# Algorithm Trading Quant Bot (project management)
---

Welcome to the project management page of the Algorithm Trading Quant Bot, where i'll be trying to keep myself organized and focused along the journey.

---

## Roadmap

### Phase 1: The Sandbox (First 3-6 Months)
- Goal: Build a robust, event-driven backtester.
- Tech Stack: Python is your best friend. Use NumPy, Pandas, Matplotlib, and Scikit-learn.
- Project:
    1. Get historical daily or hourly data for a few ETFs (e.g., SPY, GLD, TLT).
    2. Build a simple event-driven backtester from scratch or using a library like backtrader or Zipline-reloaded.
    3. Implement a simple strategy, like a moving average crossover or a basic pairs trade between two correlated assets (e.g., Pepsi vs. Coke).
    4. Focus on analysis: plot equity curves, calculate Sharpe Ratio, max drawdown, and other metrics. Learn to distrust your results and find the flaws.

### Phase 2: The Prototype (Next 6-9 Months)
- Goal: Build out the full, modular architecture and connect it to a live "paper trading" account.
- Tech Stack:
    - Broker: Open an account with Alpaca. Their API is modern, free, and perfect for this stage.
    - Database: Start using a simple database (SQLite or PostgreSQL) to store historical data, trades, and performance logs.
    - Code Structure: Refactor your sandbox code into the modular architecture described above (Data Handler, Strategy, Risk, Execution).
- Project:
    1. Implement a more sophisticated strategy. A Kalman filter-based mean reversion strategy is a fantastic project.
    2. Connect system to Alpaca's paper trading endpoint. Your bot will now run in real-time, making fake trades based on live data.
    3. Build a simple dashboard (using Streamlit or Dash) to monitor your bot's status, positions, and logs.

### Phase 3: The Live Experiment (Advanced)
- Goal: Optimize for performance and potentially deploy with a very small amount of real money (money you are 100% prepared to lose).
- Tech Stack:
    - Performance: Identify bottlenecks. Rewrite performance-critical code (like your strategy calculation or backtesting loop) in C++ and create Python bindings, or use Numba/Cython.
    - Infrastructure: Consider running your bot on a cloud server (AWS, GCP) for 24/7 uptime.
- Project:
    1. Refine your risk management module. This is what will keep you alive.
    2. Start A/B testing strategies against each other.
    3. If—and only if—your system has been profitable and stable in paper trading for months and you have thoroughly analyzed its failure modes, you might consider deploying it with a small amount of capital.

--- 

## Task Tracking

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