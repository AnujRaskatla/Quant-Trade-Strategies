# Quant-Trade-Strategies

Welcome to the Quantitative Trading Strategies repository! This collection features a variety of Python-based trading strategies for analyzing financial markets. Each strategy is accompanied by thorough documentation and organized code, allowing for easy understanding, customization, and implementation.

## Table of Contents

- [Overview](#1-overview)
- [Getting Started](#2-getting-started)
- [Directory Structure](#3-directory-structure)
- [Usage](#4-usage)
- [Strategies](#5-strategies)
- [ML Prediction Models](#6-ml-prediction-models)
- [Options Strategies](#7-options-strategies)
- [Backtesting](#8-backtesting)
- [Results](#9-results)
- [Dependencies](#10-dependencies)
- [Contributing](#11-contributing)
- [License](#12-license)
- [Acknowledgments](#13-acknowledgments)

### 1. Overview

- This repository aims to explore and implement quantitative trading strategies for financial markets.
- Strategies are designed to leverage historical market data to make informed trading decisions.
- Implemented in Python, the code is well-structured and documented for users to easily comprehend and adapt.

### 2. Getting Started

- To get started, clone this repository to your local machine.
  
  ```bash
   git clone https://github.com/AnujRaskatla/Quant-Trade-Strategies.git
- Install dependencies by running `pip install -r requirements.txt`.
- Follow the instructions in the README files of individual strategy directories.

### 3. Directory Structure

- [**data/**](data): Contains sample datasets and instructions on obtaining market data.
- [**strategies/**](strategies): Each subdirectory represents a different trading strategy.
- [**backtesting/**](backtesting): Includes scripts for evaluating strategy performance.
  
### 4. Usage
  1. Replace `your_data.csv` in the script with the actual file path or URL of your historical stock price data.
  2. The data should contain at least the following columns:

    Date:                       Date of the stock price data.
    Open, High, Low, Close:     Stock price details.
    Volume:                     Trading volume.
    Ensure that the 'Date' column is in datetime format. If not, convert it using pd.to_datetime().
  3. Run the script: `your_strategy_script.py`
  4. View the model evaluation results and visualization in the console and generated plot.

## 5. Strategies

- **MeanReversion/**: Implements a mean-reversion trading strategy.
  - `README.md`: Detailed explanation of the strategy, parameters, and logic.
  - `mean_reversion.py`: Python script containing the strategy code.

- **TrendFollowing/**: Implements a trend-following trading strategy.
  - `README.md`: Comprehensive overview of the strategy.
  - `trend_following.py`: Python script for the strategy.
    
- **SMA (Simple Moving Average):** based on SMA crossovers, aiming to generate buy and sell signals.
  - [README.md](strategies/SMA/ReadMe.md): Comprehensive overview of the strategy.
  - [sma_script.py](strategies/SMA/sma_script.py): Python script containing the strategy.

- **Pair Trading/**: based on z-score, aiming to generate buy and sell signals after threshold.
  - [README.md](strategies/Pair_Trading/README.md): Comprehensive overview of the strategy.
  - [pt.py](strategies/Pair_Trading/pt.py): Python script containing the strategy.
  - 
- **MACD x RSI/**: Used indicators - MACD and RSI to generate buy and sell signals.
  - [README.md](strategies/MACD_x_RSI/README.md): Comprehensive overview of the strategy.
  - [macd.py](strategies/MACD_x_RSI/macd.py): Python script containing the strategy.
    
## 6. ML Prediction Models
- **Random Forest Regressor Strategy/**: utilizes a Random Forest Regressor to predict stock prices based on historical data
  - [README.md](strategies/ML_Model/README.md): Comprehensive overview of the strategy.
  - [ML_script.py](strategies/ML_Model/ML_script.py): Python script containing the strategy.
    
## 7. Options Strategies

- **Covered Call Strategy/**: involves owning shares of a particular stock and selling call options against those shares.
  - [README.md](Options_Strategies/Covered_Call_Strategy/README.md): Comprehensive overview of the strategy.
  - [CC_script.py](Options_Strategies/Covered_Call_Strategy/CC_script.py): Python script containing the strategy.

### 8. Backtesting

- The [backtesting/](backtesting) directory contains scripts for evaluating the performance of each strategy.
- Detailed instructions on running backtests are provided in the [README.md](backtesting/README.md).

### 9. Results

- Visualizations and performance metrics for each strategy are available in this section.
- Backtest results demonstrate the effectiveness of the implemented strategies.

### 10. Dependencies:

- Key dependencies include pandas, numpy, and matplotlib.
```bash
pip install pandas numpy matplotlib
```
- View the `requirements.txt` file for a complete list with version information.

### 11. Contributing:

- Contributions are welcome! Please follow the guidelines outlined in the CONTRIBUTING.md file.
- Submit issues, feature requests, or pull requests to contribute to the project's development.

### 12. License:

- This project is licensed under the MIT License. See the LICENSE.md file for details.

### 13. Acknowledgments:

- Gratitude to the open-source community and contributors.
- Acknowledgments to external libraries and data sources used in the project.
