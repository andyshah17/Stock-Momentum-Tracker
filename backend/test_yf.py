import yfinance as yf

data = yf.Ticker("AAPL").history(period="1d")
print(data)
