import unittest
import pandas as pd
from stock import Stock

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

if __name__ == '__main__':
    unittest.main()
