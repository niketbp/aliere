import requests

BASE_URL = 'https://www.alphavantage.co/query?'
API_KEY = '9YI4'


def get_ticker_data(ticker):
    function = 'function=TIME_SERIES_DAILY'
    symbol = 'symbol=' + ticker
    api_key = 'apikey=' + API_KEY

    params = '&'.join([function, symbol, api_key])

    url = BASE_URL + params

    r = requests.get(url)
    content = r.json()
    most_recent = content['Meta Data']['3. Last Refreshed']
    most_recent_stock_data = content['Time Series (Daily)'][most_recent]

    return {
        'open': most_recent_stock_data['1. open'],
        'high': most_recent_stock_data['2. high'],
        'low': most_recent_stock_data['3. low'],
        'current': most_recent_stock_data['4. close']
    }

