from stock import Stock
from portfolio import Portfolio
from risk_analysis import RiskAnalysisTool
import pandas as pd

def main():
    # Load the historical prices data
    df = pd.read_excel('historical_prices.xlsx')

    # Create a Stock instance for each unique symbol in the data
    symbols = df['Symbol'].unique()
    stocks = {symbol: Stock(symbol, symbol) for symbol in symbols}  # name is the same as symbol

    # Retrieve historical prices for each stock
    for symbol, stock in stocks.items():
        stock_data = df[df['Symbol'] == symbol]
        stock.retrieve_historical_prices(stock_data)

    # Create a Portfolio and add some stocks to it
    portfolio = Portfolio()
    for stock in stocks.values():
        portfolio.add_stock(stock, 1/len(stocks))  # Equal allocation to each stock

    # Use the RiskAnalysisTool to analyze the portfolio
    risk_tool = RiskAnalysisTool(portfolio)
    var = risk_tool.calculate_var()
    print(f'Value at Risk: {var}')
    cvar = risk_tool.calculate_cvar()
    print(f'Conditional Value at Risk: {cvar}')

    # Start the Dash application
    import stock_visualizer
    stock_visualizer.app.run_server(debug=False)

if __name__ == '__main__':
    main()
