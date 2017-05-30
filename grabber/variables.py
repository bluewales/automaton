import datetime
from grabber.stock_grabber import StockGrabber


class Variables:

    def __init__(self):

        self.sg = StockGrabber()


        self.variables = [
            {
                'name': "day_of_week",
                'description': "the day of the week, a number 0-6",
                'type': "calendar",
                'fetcher': lambda day: day.weekday()
            },
            {
                'name': "day",
                'description': "the day part of the date",
                'type': "calendar",
                'fetcher': lambda day: day.day
            },
            {
                'name': "month",
                'description': "the month part of the date",
                'type': "calendar",
                'fetcher': lambda day: day.month
            },
            {
                'name': "year",
                'description': "the year part of the date",
                'type': "calendar",
                'fetcher': lambda day: day.year
            },
            {
                'name': "GOOG Open",
                'description': "opening price of google stock",
                'type': "stock",
                'fetcher': lambda day: self.sg.fetch_stock_data("GOOG", day, "Open")
            }
        ]

    def get_variable_list(self):
        return self.variables
