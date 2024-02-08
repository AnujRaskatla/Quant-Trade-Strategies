import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import coint

# Load historical stock data from CSV files
stock_a_data = pd.read_csv(r'path_to_your_csv.file', index_col='Date', parse_dates=True) # Example: C:\Users\Your Name\Desktop\stock.csv
stock_b_data = pd.read_csv(r'path_to_your_csv.file', index_col='Date', parse_dates=True)

data = pd.DataFrame({'StockA': stock_a_data['Close'], 'StockB': stock_b_data['Close']})

# Calculate the spread between Stock A and Stock B
spread = data['StockA'] - data['StockB']

# Calculate the z-score of the spread
zscore = (spread - np.mean(spread)) / np.std(spread)

# Define entry and exit points based on z-score thresholds
entry_threshold = 1.0
exit_threshold = 0.0

# Initialize positions
data['PositionA'] = 0
data['PositionB'] = 0

# Generate signals and positions
data.loc[zscore > entry_threshold, 'PositionA'] = -1  # Short Stock A
data.loc[zscore < -entry_threshold, 'PositionA'] = 1   # Long Stock A
data['PositionB'] = -data['PositionA']                # Opposite position for Stock B

# Plot the stock prices, z-score, and trading signals
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)

# Plot stock prices
ax1.plot(data.index, data['StockA'], label='Stock A')
ax1.plot(data.index, data['StockB'], label='Stock B')
ax1.set_title('Stock Prices')
ax1.legend()

# Plot z-score and trading signals
ax2.plot(data.index, zscore, label='Z-Score', color='blue')
ax2.axhline(entry_threshold, color='r', linestyle='--', label='Entry Threshold')
ax2.axhline(-entry_threshold, color='r', linestyle='--')
ax2.axhline(exit_threshold, color='g', linestyle='--', label='Exit Threshold')
ax2.axhline(-exit_threshold, color='g', linestyle='--')

# Plot Buy (^) and Sell (v) signals
ax2.scatter(data.index[data['PositionA'] == 1], zscore[data['PositionA'] == 1], marker='^', color='g', label='Buy Signal')
ax2.scatter(data.index[data['PositionA'] == -1], zscore[data['PositionA'] == -1], marker='v', color='r', label='Sell Signal')

ax2.set_title('Z-Score and Trading Signals')
ax2.legend()

plt.show()
