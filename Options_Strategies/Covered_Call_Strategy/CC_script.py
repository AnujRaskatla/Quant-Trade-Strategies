import matplotlib.pyplot as plt

# Define parameters
stock_price = 50  # Current stock price of Company XYZ
strike_price = 55  # Strike price of the call option
premium_per_share = 2  # Premium received per share for selling the call option
shares_owned = 100  # Number of shares owned

# Calculate total premium received
total_premium = premium_per_share * shares_owned

# Define expiration scenarios
stock_price_at_expiration = [45, 50, 55, 60]  # Possible stock prices at expiration

# Define lists to store outcomes and incomes
outcomes = []
total_incomes = []
colors = []

# Loop over each scenario
for price in stock_price_at_expiration:
    # Determine option exercise outcome and calculate total income
    if price < strike_price:
        option_outcome = "Option expires worthless"
        total_income = total_premium
        color = 'red'  # Color for option expiring worthless
    else:
        option_outcome = "Option exercised"
        proceeds_from_shares = strike_price * shares_owned
        total_income = proceeds_from_shares + total_premium
        color = 'green'  # Color for option being exercised
    
    # Store outcomes and incomes
    outcomes.append(option_outcome)
    total_incomes.append(total_income)
    colors.append(color)

# Plot outcomes and total incomes
plt.figure(figsize=(10, 6))
bars = plt.bar(stock_price_at_expiration, total_incomes, color=colors)
plt.xlabel('Stock Price at Expiration ($)')
plt.ylabel('Total Income ($)')
plt.title('Covered Call Strategy Outcomes')

for bar, income, price in zip(bars, total_incomes, stock_price_at_expiration):
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), f'{income}', ha='center', va='bottom')
  

# Add legend
plt.legend(handles=[plt.Rectangle((0,0),1,1, color='red', label='Option expires worthless'),
                    plt.Rectangle((0,0),1,1, color='green', label='Option exercised')],
           loc='upper left')

#plt.grid(True)
plt.show()
