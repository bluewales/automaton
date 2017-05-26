import datetime


class Variables:

    def __init__(self):


        self.variables = [
            {
                'name': "day_of_week",
                'description': "the day of the week, a number 0-6",
                'type': "calendar",
                'fetcher': lambda date: date.weekday()
            },
            {
                'name': "day",
                'description': "the day part of the date",
                'type': "calendar",
                'fetcher': lambda date: date.day
            },
            {
                'name': "month",
                'description': "the month part of the date",
                'type': "calendar",
                'fetcher': lambda date: date.month
            },
            {
                'name': "year",
                'description': "the year part of the date",
                'type': "calendar",
                'fetcher': lambda date: date.year
            }
        ]

    def get_variable_list(self):
        return self.variables
