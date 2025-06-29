import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

WINDOW_SIZE = 1

df = pd.read_csv("data/pepe_merged_data.csv")
df = df.dropna()
df["Close"] = df["Close"].astype(float)
df["Log_Close"] = np.log(df["Close"])
df["Avg_Sentiment"] = df["Avg_Sentiment"].astype(float)

X, y = [], []

for i in range(WINDOW_SIZE, len(df)):
    window = df.iloc[i - WINDOW_SIZE:i]
    features = np.concatenate([window["Log_Close"].values, window["Avg_Sentiment"].values])
    X.append(features)
    y.append(df.iloc[i]["Log_Close"])

X, y = np.array(X), np.array(y)

# confirm arrays
print("X shape:", X.shape)
print("y shape:", y.shape)

# split and train
X_train, X_test, y_train, y_test = train_test_split(X, y, shuffle=False, test_size=0.2)
model = Ridge() # simple linear regression with regularization
model.fit(X_train, y_train)

# predict
y_pred = model.predict(X_test)

actual_prices = np.exp(y_test)
predicted_prices = np.exp(y_pred)

# evaluate
mse = mean_squared_error(actual_prices, predicted_prices)
rmse = np.sqrt(mse)
print(f"RMSE: {rmse:.8f}")

prediction_df = pd.DataFrame({
    "Date": df.iloc[-len(y_test):]["Date"].values,
    "Actual_Log_Price": y_test,
    "Predicted_Log_Price": y_pred
})
prediction_df["Actual_Price"] = np.exp(prediction_df["Actual_Log_Price"])
prediction_df["Predicted_Price"] = np.exp(prediction_df["Predicted_Log_Price"])

prediction_df.to_csv("data/pepe_predictions.csv", index=False)
print("Saved predictions to data/pepe_predictions.csv")

# plot
plt.plot(actual_prices, label="Actual Price")
plt.plot(predicted_prices, label="Predicted Price")
plt.title("Predicted vs. Actual Prices (exp scale)")
plt.xlabel("Day")
plt.ylabel("Price")
plt.legend()
plt.show()

