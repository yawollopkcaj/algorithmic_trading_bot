import bt
import pandas as pd

# load signals 
# df = pd.read_csv("data/pepe_signals.csv")
# df["Date"] = pd.to_datetime(df["Date"])
# df.set_index("Date", inplace=True)

# price = df["Actual_Price"]

# signals = df["Signal"].copy()
# positions = signals.replace({"BUY": 1, "SELL": -1, "HOLD": 0}).fillna(0)

# Assume signals.csv has Date and Signal columns
signals = pd.read_csv("data/pepe_signals.csv", parse_dates=["Date"], index_col="Date")
prices = pd.read_csv("data/pepe_price_data.csv", parse_dates=["Date"], index_col="Date")

# Convert signals to numeric weights
positions = signals["Signal"].replace({"BUY": 1, "SELL": -1, "HOLD": 0})

# Convert to a DataFrame with ticker column
weights = pd.DataFrame(data=positions.values, index=positions.index, columns=["PEPE"])


def signal_strategy():
    signal_series = positions

    # Create a strategy with slippage (0.2% per trade)
    return bt.Strategy(
        "PEPE Strategy",
        [
            bt.algos.WeighTarget(weights),
            bt.algos.RunDaily(),
            bt.algos.Rebalance()
        ],
    )

# Backtest
price_series = pd.DataFrame({"PEPE": prices})
portfolio = bt.Backtest(signal_strategy(), price_series)

# Run
result = bt.run(portfolio)

# Display
result.plot(title="PEPE Strategy Backtest")
print(result.display())