# SMA Backtesting Script

This Python script performs a simple backtest of a trading strategy based on the Simple Moving Average (SMA) crossover. The script reads historical stock price data from a CSV file, calculates SMA values, generates buy and sell signals, and performs a basic backtest to evaluate the strategy's performance.

## Prerequisites

Before running the script, ensure you have the following installed:

- Python 3
- Required Python libraries: pandas, numpy, matplotlib

You can install the required libraries using the following command:

```bash
pip install pandas numpy matplotlib

## Usage

1. **Clone the repository or download the script.**

2. **Prepare your historical stock price data in CSV format and update the script with the correct file path.**

3. **Open a terminal or command prompt and navigate to the directory containing the script.**

4. **Run the script:**

    ```bash
    python your_script_name.py
    ```

    Replace `your_script_name.py` with the actual name of your backtesting script.

5. **Review the output:**
   - The script will display the initial and final balance after the backtest.
   - A plot will be generated showing the SMA strategy, buy signals (green triangles), and sell signals (red triangles).

## Customization

You can customize the script by adjusting the following parameters within the script:

- `initial_balance`: Initial balance in dollars for the backtest.
- File path to your CSV file containing historical stock price data.
- Any additional parameters specific to your SMA strategy, such as the window size for calculating SMA.

Feel free to modify the script to suit your specific needs or integrate it into a larger trading strategy framework.

## Disclaimer

This script is a simplified example for educational purposes only. It does not account for transaction costs, slippage, or other factors that may affect real-world trading strategies. Use it responsibly and consider seeking professional advice before deploying any trading strategies.

Happy backtesting!
