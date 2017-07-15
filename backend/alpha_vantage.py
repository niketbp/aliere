import requests


class AlphaVantage:

    def __init__(self):
        self.__BASE_URL = 'https://www.alphavantage.co/query?'
        self.__API_KEY = '9YI4'

    def get_ticker_data(self, ticker):
        function = 'function=TIME_SERIES_DAILY'
        symbol = 'symbol=' + ticker
        api_key = 'apikey=' + self.__API_KEY

        params = '&'.join([function, symbol, api_key])

        url = self.__BASE_URL + params

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
