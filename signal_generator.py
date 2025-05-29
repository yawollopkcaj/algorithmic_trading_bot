import numpy as np
import pandas as pd

TRANSACTION_COST = 0.03 # 3%

def load_predictions(path="data/pepe_predictions.csv"):
    df = pd.read_csv(path)
    df["Actual_Price"] = df["Actual_Price"].astype(float)
    df["Predicted_Price"] = df["Predicted_Price"].astype(float)
    return df


def generate_signals(df):
    signals = []
    for pred, actual in zip(df["Predicted_Price"], df["Actual_Price"]):

        if pred > actual * (1 + TRANSACTION_COST):
            signals.append("BUY")
        elif pred < actual * (1 - TRANSACTION_COST):
            signals.append("SELL")
        else:
            signals.append("HOLD")
    df["Signal"] = signals
    return df


def save_signals(df, path="data/pepe_signals.csv"):
    df.to_csv(path, index=False)
    print(f"Saved signals to {path}")


if __name__ == "__main__":
    df = load_predictions()
    df = generate_signals(df)
    save_signals(df)
    print(df[["Date", "Actual_Price", "Predicted_Price", "Signal"]].tail())