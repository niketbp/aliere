import requests

ALPHA_VANTAGE_KEY = '9YI4'

class AlphaVantage():

    def __init__(self):
        self.__BASE_URL = 'https://www.alphavantage.co/query?'

    def get_ticker_data(self, symbol):
        function = 'function=TIME_SERIES_DAILY'
        symbol = 'symbol=' + symbol
        api_key = 'apikey=' + ALPHA_VANTAGE_KEY

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
