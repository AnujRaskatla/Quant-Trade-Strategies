import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv(r'C:\Users\Anuj Raskatla\Desktop\st.csv')

SMA30 = pd.DataFrame()
SMA30['High'] = df['High'].rolling(window=30).mean()
SMA100 = pd.DataFrame()
SMA100['High'] = df['High'].rolling(window=100).mean()

Data = pd.DataFrame()
Data['SMA30'] = SMA30['High']
Data['SMA100'] = SMA100['High']

def buysell(Data):
    b = []
    s = []
    f = -1
    for i in range(len(Data)):
        if i > 2 and Data['SMA30'][i - 1] > Data['SMA30'][i]:
            if f == 1:
                s.append(Data['SMA30'][i])
                b.append(np.nan)
                f = -1
            else:
                b.append(np.nan)
                s.append(np.nan)
        elif Data['SMA30'][i] > Data['SMA100'][i]:
            if f != 1:
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

bs = buysell(Data)
Data['b'] = bs[0]
Data['s'] = bs[1]

plt.plot(Data['SMA30'], label='30')
plt.plot(Data['SMA100'], label='100')
plt.scatter(Data.index, Data['b'], label='buy', marker='^', color='Green')
plt.scatter(Data.index, Data['s'], label='Sell', marker='v', color='Red')

plt.xlabel('X')
plt.ylabel('Y')

plt.legend(loc='upper left')
plt.show()
