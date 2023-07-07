import pandas as pd

# Portfolio class to manage a portfolio of stocks
class Portfolio:
    def __init__(self):
        self.stocks = []  # List to store the stocks in the portfolio
        self.allocation = []  # List to store the allocation for each stock in the portfolio
        self.historical_prices = []  # List to store historical prices of the portfolio

    # Method to add a stock to the portfolio
    def add_stock(self, stock, allocation):
        self.stocks.append(stock)
        self.allocation.append(allocation)

    # Method to remove a stock from the portfolio
    def remove_stock(self, stock):
        index = self.stocks.index(stock)
        self.stocks.pop(index)
        self.allocation.pop(index)

    # Method to retrieve historical prices for the stocks in the portfolio
    def retrieve_historical_prices(self, historical_prices_df):
        for stock in self.stocks:
            stock.retrieve_historical_prices(historical_prices_df)

    # Method to calculate returns of the portfolio
    def calculate_portfolio_returns(self):
        portfolio_returns = []  # List to store portfolio returns
        # Calculate the return for each stock and weight it by the stock's allocation in the portfolio
        for stock, allocation in zip(self.stocks, self.allocation):
            stock_returns = stock.calculate_returns()
            weighted_returns = [allocation * r for r in stock_returns]
            portfolio_returns.append(weighted_returns)
        # Sum the returns across stocks for each day to get the portfolio return for that day
        return [sum(returns) for returns in zip(*portfolio_returns)]

    # Method to calculate the volatility of the portfolio
    # Simplification as we would need to use covariance to calculate the volatility of the portfolio. we can add that later
    def calculate_portfolio_volatility(self):
        portfolio_volatility = 0
        for stock, allocation in zip(self.stocks, self.allocation):
            stock_volatility = stock.calculate_volatility()
            portfolio_volatility += allocation * stock_volatility
        return portfolio_volatility
