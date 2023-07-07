import pandas as pd

# Stock class to store information about a particular stock
class Stock:
    def __init__(self, symbol, name):
        self.symbol = symbol
        self.name = name
        self.historical_prices = []
        self.historical_dates = []  # list to store dates

    def retrieve_historical_prices(self, historical_prices_df):
        # Retrieve historical prices and dates from the DataFrame
        stock_data = historical_prices_df[historical_prices_df['Symbol'] == self.symbol]
        self.historical_prices = stock_data['Close'].tolist()
        self.historical_dates = pd.to_datetime(stock_data['Date']).tolist()  # assuming you have a 'Date' column

    # Method to calculate daily returns of the stock
    def calculate_returns(self):
        returns = []  # Empty list to store daily returns
        for i in range(1, len(self.historical_prices)):
            daily_return = (self.historical_prices[i] - self.historical_prices[i-1]) / self.historical_prices[i-1]
            returns.append(daily_return)
        return returns

    # Method to calculate the volatility of the stock
    def calculate_volatility(self):
        # Volatility is the standard deviation of returns
        returns = self.calculate_returns()  # Get the daily returns
        mean_return = sum(returns) / len(returns)  # Calculate the average return
        # Calculate the squared deviation from the mean return for each return, take the average of these and get the square root
        volatility = (sum([(r - mean_return) ** 2 for r in returns]) / len(returns)) ** 0.5
        return volatility
