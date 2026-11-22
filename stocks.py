import pandas as pd
import yfinance as yf
stock_df = yf.Ticker("MSFT").history(period = '1mo')["Close"]
stock_df["dates"] = pd.to_datetime(stock_df.index)
stock_df["dates"] = stock_df.index.date
stock_df.to_csv("microsoft_past_prices.csv")
