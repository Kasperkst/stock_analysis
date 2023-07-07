import yfinance as yf
import pandas as pd
import random

# Define the stock symbols
stocks = ["NVO", "AAPL", "MSFT", "TSLA", "^GSPC"]

# Retrieve historical prices for each stock
dfs = []
for stock in stocks:
    data = yf.download(stock, start="2004-01-01", end="2023-06-29")
    df = pd.DataFrame(data)
    df["Symbol"] = stock  # Add a column to identify the stock symbol
    dfs.append(df)

# Concatenate all the stock data into a single DataFrame
historical_prices = pd.concat(dfs)

# Define the file path
#file_path = r"C:\Users\kaspe\Desktop\python_projects\financial_risk\historical_prices.xlsx"
filename = "historical_prices.xlsx"


# Save DataFrame to Excel file
historical_prices.to_excel(filename, index=False)