import requests
import json
import os

def calStockService(symbol = "IBM"):
    # Replace YOUR_API_KEY with your actual Alpha Vantage API key
    api_key = os.getenv('ALPHA_KEY')

    # Specify the interval (time frame) of the data
    interval = "5min"

    # Specify the type of data you want to retrieve
    function = "TIME_SERIES_INTRADAY"

    # Construct the API endpoint URL
    url = f"https://www.alphavantage.co/query?function={function}&symbol={symbol}&interval={interval}&apikey={api_key}"
    print(url)
    # Make an API request and get the response
    response = requests.get(url)

    # Parse the JSON data from the response
    data = json.loads(response.text)

    # Print the data
    print(data)
