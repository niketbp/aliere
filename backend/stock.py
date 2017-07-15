from globals import alpha_vantage

class Stock:

    def __init__(self):
        pass

    def get_stock_data(self, ticker):
        return alpha_vantage.get_ticker_data(ticker)
