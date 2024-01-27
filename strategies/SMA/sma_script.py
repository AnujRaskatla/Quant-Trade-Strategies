# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the dataset (replace path with the appropriate file path or URL)
df = pd.read_csv(r'path_to_your_csv.file') # Example: C:\Users\Your Name\Desktop\stock.csv

# Calculate the 30-day Simple Moving Average (SMA)
SMA30 = pd.DataFrame()
SMA30['High'] = df['High'].rolling(window=30).mean()

# Calculate the 100-day Simple Moving Average (SMA)
SMA100 = pd.DataFrame()
SMA100['High'] = df['High'].rolling(window=100).mean()

# Create a DataFrame to store SMA values
Data = pd.DataFrame()
Data['SMA30'] = SMA30['High']
Data['SMA100'] = SMA100['High']

# Function to generate buy and sell signals based on SMA crossovers
def buysell(Data):
    b = []  # List to store buy signals
    s = []  # List to store sell signals
    f = -1  # Flag to track position (1 for long, -1 for short, -1 for no position)
    
    for i in range(len(Data)):
        # Check for a crossover of SMA30 over SMA100 (potential buy signal)
        if i > 2 and Data['SMA30'][i - 1] > Data['SMA30'][i]:
            if f == 1:  # If already in a long position, generate sell signal
                s.append(Data['SMA30'][i])
                b.append(np.nan)
                f = -1
            else:
                b.append(np.nan)
                s.append(np.nan)
        # Check for a crossover of SMA30 under SMA100 (potential sell signal)
        elif Data['SMA30'][i] > Data['SMA100'][i]:
            if f != 1:  # If not in a long position, generate buy signal
                b.append(Data['SMA30'][i])
                s.append(np.nan)
                f = 1
            else:
                b.append(np.nan)
                s.append(np.nan)
        else:
            b.append(np.nan)
            s.append(np.nan)
    
    return b, s

# Generate buy and sell signals using the defined function
bs = buysell(Data)
Data['b'] = bs[0]  # Buy signals
Data['s'] = bs[1]  # Sell signals

# Plotting the SMA strategy
plt.plot(Data['SMA30'], label='30-day SMA')
plt.plot(Data['SMA100'], label='100-day SMA')
plt.scatter(Data.index, Data['b'], label='Buy', marker='^', color='Green')
plt.scatter(Data.index, Data['s'], label='Sell', marker='v', color='Red')
plt.xlabel('Time period')
plt.ylabel('Price')
plt.legend(loc='upper left')
plt.show()
