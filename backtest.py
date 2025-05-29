import bt
import pandas as pd

# load signals 
df = pd.read_csv("data/pepe_signals.csv")
df["Date"] = pd.to_datetime(df["Date"])
df.set_index("Date", inplace=True)

price = df["Actual_Price"]

signals = df["Signal"].copy()
positions = signals.replace({"BUY": 1, "SELL": -1, "HOLD": 0}).fillna(0)

def signal_strategy():
    signal_series = positions

    # Create a strategy with slippage (0.2% per trade)
    return bt.Strategy(
        "PEPE Strategy",
        [
            bt.algos.WeighTarget(signal_series),
            bt.algos.RunDaily(),
            bt.algos.Rebalance()
        ],
    )

# Backtest
price_series = pd.DataFrame({"PEPE": price})
portfolio = bt.Backtest(signal_strategy(), price_series)

# Run
result = bt.run(portfolio)

# Display
result.plot(title="PEPE Strategy Backtest")
print(result.display())