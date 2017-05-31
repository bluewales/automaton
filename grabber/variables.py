import datetime
from grabber.stock_grabber import StockGrabber


class Variables:

    def __init__(self):

        self.sg = StockGrabber()

        self.variables = [
            {
                'name': "day_of_week",
                'description': "day of the week, a number 0-6",
                'type': "calendar",
                'fetcher': lambda day: day.weekday()
            },
            {
                'name': "day",
                'description': "day part of the date",
                'type': "calendar",
                'fetcher': lambda day: day.day
            },
            {
                'name': "month",
                'description': "month part of the date",
                'type': "calendar",
                'fetcher': lambda day: day.month
            },
            {
                'name': "year",
                'description': "year part of the date",
                'type': "calendar",
                'fetcher': lambda day: day.year
            },
            {
                'name': "GOOG Open",
                'description': "opening price of google stock",
                'type': "stock",
                'fetcher': lambda day: self.sg.fetch_stock_data("GOOG", day, "Open")
            },
            {
                'name': "GOOG High",
                'description': "high price of google stock",
                'type': "stock",
                'fetcher': lambda day: self.sg.fetch_stock_data("GOOG", day, "High")
            },
            {
                'name': "GOOG Low",
                'description': "low price of google stock",
                'type': "stock",
                'fetcher': lambda day: self.sg.fetch_stock_data("GOOG", day, "Low")
            },
            {
                'name': "GOOG Close",
                'description': "close price of google stock",
                'type': "stock",
                'fetcher': lambda day: self.sg.fetch_stock_data("GOOG", day, "Close")
            },
            {
                'name': "GOOG Volume",
                'description': "trade volume of google stock",
                'type': "stock",
                'fetcher': lambda day: self.sg.fetch_stock_data("GOOG", day, "Volume")
            }
        ]

    def get_variable_list(self):
        return self.variables
