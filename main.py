import yfinance as yf
import streamlit as st
import pandas as pd


st.write("""
#Simple Stock price App by Samoilov Kirill

Showing are the stock closing price and volume of Google!

""")  # header of App

tickerSymbol = 'GOOGL'  # define the ticker symbol
tickerData = yf.Ticker(tickerSymbol)  # get data on this ticker
tickerDF = tickerData.history(period='1d', start='2010-5-31', end='2023-1-01')  # get the historical prices for this ticker
st.line_chart(tickerDF.Close)  # see your data
st.line_chart(tickerDF.Volume)



