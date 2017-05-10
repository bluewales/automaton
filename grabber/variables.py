import datetime


class Variables:

    def __init__(self):

        def get_day_of_week(date):
            return date.weekday()

        def get_day(date):
            return date.day

        def get_month(date):
            return date.month

        def get_year(date):
            return date.year

        self.variables = [
            {
                'name': "day_of_week",
                'description': "the day of the week, a number 0-6",
                'type': "calendar",
                'fetcher': get_day_of_week
            },
            {
                'name': "day",
                'description': "the day part of the date",
                'type': "calendar",
                'fetcher': get_day
            },
            {
                'name': "month",
                'description': "the month part of the date",
                'type': "calendar",
                'fetcher': get_month
            },
            {
                'name': "year",
                'description': "the year part of the date",
                'type': "calendar",
                'fetcher': get_year
            }
        ]

    def get_variable_list(self):
        return self.variables
