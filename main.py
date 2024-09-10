from datetime import datetime

class Stock:
    def __init__(self, name, prices):
        self.name = name
        self.prices = prices  # Dictionary with date as key and price as value

    def Price(self, date):
        return self.prices.get(date, 0)

class Portfolio:
    def __init__(self, stocks):
        self.stocks = stocks  # List of Stock objects

    def Profit(self, start_date, end_date):
        start_value = 0
        end_value = 0
        
        for stock in self.stocks:
            start_value += stock.Price(start_date)
            end_value += stock.Price(end_date)
        
        profit = end_value - start_value
        return profit

    def AnnualizedReturn(self, start_date, end_date):
        start_value = 0
        end_value = 0

        for stock in self.stocks:
            start_value += stock.Price(start_date)
            end_value += stock.Price(end_date)

        years = (end_date - start_date).days / 365.25
        if start_value == 0:
            return 0
        return (end_value / start_value) ** (1 / years) - 1

# Example usage:
prices_aapl = {datetime(2023, 1, 1): 150, datetime(2024, 1, 1): 200}
prices_msft = {datetime(2023, 1, 1): 250, datetime(2024, 1, 1): 300}

aapl = Stock("AAPL", prices_aapl)
msft = Stock("MSFT", prices_msft)

portfolio = Portfolio([aapl, msft])
start = datetime(2023, 1, 1)
end = datetime(2024, 1, 1)

print("Profit:", portfolio.Profit(start, end))
print("Annualized Return:", portfolio.AnnualizedReturn(start, end))
