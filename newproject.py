import yfinance as yf
import streamlit as st
import pandas as pd  # Import pandas

st.write("""
# Stock Price App 💸📈

Select a company from the dropdown menu and choose a date range to view its stock prices!

""")

# Define a dictionary of companies and their ticker symbols
companies_dict = {
    'Google': 'GOOGL',
    'Apple': 'AAPL',
    'Microsoft': 'MSFT',
    'Amazon': 'AMZN',
    'Meta': 'META',  # 'FB' is the ticker symbol for Meta
    'Tesla': 'TSLA',
    'Alphabet': 'GOOG',
    'Tata Consultancy Services': 'TCS',
    'Procter & Gamble': 'PG',
    'Coca-Cola': 'KO',
    'Wipro': 'WIPRO',
    'Infosys': 'INFY',
    # Add more companies as needed
}

# Create a dropdown menu for selecting a company
selected_company = st.selectbox('Search for a Company', list(companies_dict.keys()))

# Get the ticker symbol for the selected company
selected_ticker = companies_dict[selected_company]

# Get data on the selected company
tickerData = yf.Ticker(selected_ticker)

# Option to select a specific year
is_single_year = st.checkbox('View only one year', False)
if is_single_year:
    selected_year = st.slider('Select Year', 2010, 2024, 2024)
    selected_start_date = f'{selected_year}-1-1'
    selected_end_date = f'{selected_year}-12-31'
else:
    # Slider for selecting a date range
    selected_start_date = st.date_input('Select Start Date', value=pd.to_datetime('2010-01-01'))
    selected_end_date = st.date_input('Select End Date', value=pd.to_datetime('2024-12-31'))

# Get historical prices for the selected date range
tickerDf = tickerData.history(period='1d', start=selected_start_date, end=selected_end_date)

# Display the historical prices for the selected company and date range
st.write(f"## Stock Prices for {selected_company} ({selected_start_date} - {selected_end_date})")

# Markdown description for Closing Price
st.markdown("**Closing Price:** Displaying the trend of closing prices over time.")
# Line chart for Closing Price
st.line_chart(tickerDf.Close, use_container_width=True, color='#4CAF50')

# Markdown description for Volume
st.markdown("**Volume:** Illustrating the trading volume of stocks over time.")
# Line chart for Volume
st.line_chart(tickerDf.Volume, use_container_width=True, color='#00FFFF')
