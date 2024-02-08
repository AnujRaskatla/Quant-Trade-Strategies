import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Function to load historical price data from CSV files
def load_data(file_path):
    data = pd.read_csv(file_path, index_col='Date', parse_dates=True)
    return data['Adj Close']

# Function to calculate z-score of the spread
def calculate_zscore(spread):
    return (spread - spread.mean()) / spread.std()

# Function to generate trading signals
def generate_signals(zscore, entry_threshold=2.0, exit_threshold=0.0):
    signals = pd.Series(index=zscore.index, dtype=int)
    signals[zscore > entry_threshold] = 1  # Buy signal
    signals[zscore < -entry_threshold] = -1  # Sell signal
    signals[abs(zscore) < exit_threshold] = 0  # Exit signal
    return signals

# Main function
def main():
    # Define parameters
    # Example: C:\Users\Your Name\Desktop\stock.csv
    file_path1 = r'path_to_your_csv.file'  # CSV file path for first asset
    file_path2 = r'path_to_your_csv.file'  # CSV file path for second asset
    entry_threshold = 2.0
    exit_threshold = 0.0

    # Load historical price data
    price1 = load_data(file_path1)
    price2 = load_data(file_path2)

    # Calculate spread between the two assets' prices
    spread = price1 - price2

    # Calculate z-score of the spread
    zscore = calculate_zscore(spread)

    # Generate trading signals
    signals = generate_signals(zscore, entry_threshold, exit_threshold)
    # Plotting
    fig, ax = plt.subplots(2, 1, figsize=(10, 8), sharex=True)

    # Spread plot
    ax[0].plot(spread, label='Spread', color='blue')
    ax[0].plot(price1, label='Asset 1 (Close)', color='lightgray', alpha=0.5, linestyle='--')
    ax[0].plot(price2, label='Asset 2 (Close)', color='lightgray', alpha=0.5, linestyle='--')
    ax[0].set_ylabel('Price')
    ax[0].legend()

    # Z-score plot
    ax[1].plot(zscore, color='r', label='Z-score')
    ax[1].axhline(0, color='k', linestyle='--')
    ax[1].axhline(2, color='g', linestyle='--')
    ax[1].axhline(-2, color='g', linestyle='--')
    ax[1].set_ylabel('Z-score')

    # Plot buy and sell signals
    buy_indices = signals[signals == 1].index
    sell_indices = signals[signals == -1].index
    ax[1].scatter(buy_indices, zscore[buy_indices], marker='^', color='g', label='Buy Signal')
    ax[1].scatter(sell_indices, zscore[sell_indices], marker='v', color='r', label='Sell Signal')

    # Add legend
    ax[1].legend()

    plt.tight_layout()
    plt.show()
if __name__ == "__main__":
    main()