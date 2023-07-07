import unittest
import pandas as pd
import numpy as np
from stock import Stock
from portfolio import Portfolio
from risk_analysis import RiskAnalysisTool

class TestStock(unittest.TestCase):
    def test_stock(self):
        data = {
            "Date": pd.to_datetime(['2004-01-02', '2004-01-05']),
            "Close": [4.124000072, 4.100999832],
            "Symbol": ['NVO', 'NVO']
        }
        df = pd.DataFrame(data)

        stock = Stock('NVO', 'Novo Nordisk')
        stock.retrieve_historical_prices(df)

        self.assertEqual(stock.symbol, 'NVO')
        self.assertEqual(stock.name, 'Novo Nordisk')
        self.assertEqual(stock.historical_prices, df['Close'].tolist())
        self.assertEqual(stock.historical_dates, df['Date'].tolist())

        returns = stock.calculate_returns()
        expected_return = (df['Close'].iloc[1] - df['Close'].iloc[0]) / df['Close'].iloc[0]
        self.assertEqual(returns, [expected_return])


class TestPortfolio(unittest.TestCase):
    def test_portfolio(self):
        # Create a new portfolio
        portfolio = Portfolio()

        # Create a new stock
        stock = Stock('NVO', 'Novo Nordisk')
        stock.historical_prices = [4.124000072, 4.100999832, 4.097000122, 4.004000187]

        # Add the stock to the portfolio
        portfolio.add_stock(stock, 0.5)

        # Check that the stock was added to the portfolio
        self.assertEqual(portfolio.stocks[0], stock)
        self.assertEqual(portfolio.allocation[0], 0.5)

        # Remove the stock from the portfolio
        portfolio.remove_stock(stock)

        # Check that the portfolio is now empty
        self.assertFalse(portfolio.stocks)
        self.assertFalse(portfolio.allocation)
        
class TestRiskAnalysisTool(unittest.TestCase):
    def test_risk_analysis_tool(self):
        # Create a new portfolio
        portfolio = Portfolio()

        # Create new stocks
        stock1 = Stock('NVO', 'Novo Nordisk')
        stock1.historical_prices = [4.124000072, 4.100999832, 4.097000122, 4.004000187]
        stock2 = Stock('AAPL', 'Apple Inc.')
        stock2.historical_prices = [144.000, 147.050, 149.070, 148.500]

        # Mock returns for the stocks
        stock1.historical_returns = np.random.normal(0, 0.01, size=100)
        stock2.historical_returns = np.random.normal(0, 0.01, size=100)

        # Add the stocks to the portfolio
        portfolio.add_stock(stock1, 0.5)
        portfolio.add_stock(stock2, 0.5)

        # Create a new risk analysis tool
        risk_tool = RiskAnalysisTool(portfolio)

        # Calculate VaR and CVaR
        var = risk_tool.calculate_var(0.95)
        cvar = risk_tool.calculate_cvar(0.95)

        # Perform Monte Carlo simulation
        portfolio_values = risk_tool.perform_monte_carlo_simulation(10)

        self.assertIsInstance(var, float)
        self.assertIsInstance(cvar, float)
        self.assertEqual(len(portfolio_values), 10)

if __name__ == '__main__':
    unittest.main()
