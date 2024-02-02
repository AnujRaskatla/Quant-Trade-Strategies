# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
import matplotlib.pyplot as plt

# Step 1: Load Historical Data
data = pd.read_csv(r'path_to_your_csv.file') # Example: C:\Users\Your Name\Desktop\stock.csv


# Step 2: Data Preprocessing
# Assuming 'Date' is in datetime format, if not, convert it using pd.to_datetime()
data['Date'] = pd.to_datetime(data['Date'], dayfirst=True)
data.set_index('Date', inplace=True)

# Step 3: Feature Engineering (Example: Adding a simple moving average)
data['SMA_20'] = data['Close'].rolling(window=20).mean()


# Step 4: Train-Test Split
features = data[['Open', 'High', 'Low', 'Close', 'Volume', 'SMA_20']]
target = data['Close']

X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

# Step 5: Model Training
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Step 6: Model Evaluation
predictions = model.predict(X_test)
mae = mean_absolute_error(y_test, predictions)
print(f'Mean Absolute Error: {mae}')

# Step 7: Visualization
plt.title('ML Prediction for JBMA')
plt.plot(y_test.index, y_test, label='Actual Prices', color='blue')
plt.plot(y_test.index, predictions, label='Predicted Prices', color='red')
plt.xlabel('Date')
plt.ylabel('Stock Price')
plt.legend()
plt.show()
