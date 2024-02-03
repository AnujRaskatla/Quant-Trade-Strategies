# Stock Price Prediction using Random Forest Regressor

This repository contains a Python script that utilizes a Random Forest Regressor to predict stock prices based on historical data. The script also includes data preprocessing, feature engineering, model training, evaluation, and visualization steps.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Data](#data)
- [Features](#features)
- [Model](#model)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/stock-price-prediction.git
2. Navigate to the project directory:
	'cd stock-price-prediction'
3. Install the required libraries:
	'pip install -r requirements.txt'

## Usage
1. Replace 'your_data.csv' in the script with the actual file path or URL of your historical stock price data.

2. Run the script:
	'python stock_prediction.py'
3. View the model evaluation results and visualization in the console and generated plot.

## Data

Make sure your historical data file is in CSV format. The data should contain at least the following columns:

Date: Date of the stock price data.
Open, High, Low, Close: Stock price details.
Volume: Trading volume.
Ensure that the 'Date' column is in datetime format. If not, convert it using pd.to_datetime().

Features
The script performs the following steps:

Data Preprocessing: Converts 'Date' column to datetime format and sets it as the index.

Feature Engineering: Adds a simple moving average (SMA) with a window of 20 days.

Train-Test Split: Splits the data into training and testing sets.

Model Training: Utilizes a Random Forest Regressor with 100 estimators.

Model Evaluation: Calculates the Mean Absolute Error (MAE) on the testing set.

Visualization: Plots the actual and predicted stock prices.

Model
The script uses the Random Forest Regressor from scikit-learn with 100 estimators for predicting stock prices.

python
Copy code
model = RandomForestRegressor(n_estimators=100, random_state=42)
Results
The model's Mean Absolute Error (MAE) on the testing set is printed to the console. Additionally, a plot comparing actual and predicted stock prices is generated.

Contributing
Feel free to contribute to this project by opening issues or pull requests. Any feedback or improvements are welcome!

License
This project is licensed under the MIT License.










- **SMA (Simple Moving Average) Strategy:**
  - **Overview:**
    - This strategy is based on Simple Moving Average (SMA) crossovers, aiming to generate buy and sell signals.
  - **Parameters:**
    - Adjustable parameters include the window size for SMA calculations.
  - **Logic:**
    - Buy Signal: Generated when the 30-day SMA crosses above the 100-day SMA.
    - Sell Signal: Generated when the 30-day SMA crosses below the 100-day SMA.
  - **Code:**
    - [`sma_script.py`](sma_script.py): Python script containing the strategy code.
  - **Usage:**
    - To use this strategy, follow the instructions in the README and execute the provided Python script.
    - Adjust parameters as needed to suit your trading preferences.
  - **Example Visualization:**
    - ![SMA Strategy Example](sma_strategy_example.png)
  - **Backtesting:**
    - Refer to the `backtesting/` directory for scripts evaluating the performance of this strategy.
  - **Results:**
    - Visualizations and performance metrics for this strategy can be found in the `results/` directory.
