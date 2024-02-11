import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def calculate_macd(df, short_window=12, long_window=26, signal_window=9):
    short_ema = df['Close'].ewm(span=short_window, min_periods=1, adjust=False).mean()
    long_ema = df['Close'].ewm(span=long_window, min_periods=1, adjust=False).mean()
    macd = short_ema - long_ema
    signal_line = macd.ewm(span=signal_window, min_periods=1, adjust=False).mean()
    return macd, signal_line

def calculate_rsi(df, window=14):
    delta = df['Close'].diff(1)
    gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

# Load your data into a DataFrame 
df = pd.read_csv(r'path_to_your_csv.file') # Example: C:\Users\Your Name\Desktop\stock.csv

# Calculate MACD
macd, signal_line = calculate_macd(df)
df['MACD'] = macd
df['Signal_Line'] = signal_line

# Calculate RSI
rsi = calculate_rsi(df)
df['RSI'] = rsi

# Plotting
plt.figure(figsize=(14, 8))

# Plotting Close Price
plt.subplot(3, 1, 1)
plt.plot(df['Date'], df['Close'], label='Close Price', color='blue')
plt.title('Close Price')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()

# Plotting MACD and Signal Line
plt.subplot(3, 1, 2)
plt.plot(df['Date'], df['MACD'], label='MACD', color='red')
plt.plot(df['Date'], df['Signal_Line'], label='Signal Line', color='green')
plt.title('MACD and Signal Line')
plt.xlabel('Date')
plt.ylabel('MACD')
plt.legend()

# Plotting RSI
plt.subplot(3, 1, 3)
plt.plot(df['Date'], df['RSI'], label='RSI', color='purple')
plt.title('RSI')
plt.xlabel('Date')
plt.ylabel('RSI')
plt.legend()

plt.tight_layout()
plt.show()
