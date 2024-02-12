# Covered Call Strategy:
  - **Overview:**
    - The covered call strategy involves owning shares of a particular stock and selling call options against those shares. The script plots the total income generated from the strategy under different scenarios of the stock price at expiration.buy and sell signals.
  - **Parameters:**
    - `Stock Price`: Current price of the underlying stock (e.g., Company XYZ).
`Strike Price` : The predetermined price at which the call option can be exercised.
`Premium per Share` : The amount received per share for selling the call option.
`Shares Owned` : Number of shares owned by the investor.
  - **Logic:**
    - If the stock price remains below the strike price at expiration, the call option expires worthless, and the investor keeps the premium received. They can then sell more call options to generate additional income.
If the stock price rises above the strike price but remains below the total income generated from the premium and the difference between the strike price and the current stock price, the option will likely be exercised, and the investor will sell their shares at the strike price. They still keep the premium received, which adds to their profit.
If the stock price rises significantly above the strike price, the option may be exercised, and the investor sells their shares at the strike price. However, their profit potential is capped at the strike price plus the premium received, potentially missing out on further upside beyond that point.
  - **Code:**
    - [sma_script.py](sma_script.py): Python script containing the strategy code.
  - **Usage:**
    - Ensure you have Python installed on your system.
Clone or download this repository to your local machine.
Open the Python script (covered_call_strategy.py) in an IDE or text editor.
Modify the parameters as per your investment strategy (e.g., stock price, strike price, premium per share, shares owned).
Run the script. It will generate a plot showing the outcomes of the covered call strategy under different scenarios of the stock price at expiration.
  - **Example Visualization:**
    - ![SMA Strategy Example](sma_strategy_example.png)
  - **Backtesting:**
    - Refer to the [backtesting/](backtesting/SMA) directory for scripts evaluating the performance of this strategy.
  - **Results:**
    - Visualizations and performance metrics for this strategy can be found in the `results/` directory.
- **Note:**
    - This script serves as a tool for visualizing the potential outcomes of a covered call strategy. It is important to conduct thorough research and analysis before implementing any investment strategy.
The provided parameters and scenarios are for demonstration purposes only. Adjust them according to your specific investment goals and market conditions.
