import requests
import datetime
import json
from datetime import timedelta, date
from dateutil.relativedelta import relativedelta


def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)


class StockGrabber:
    def __init__(self):
        self.example_url = "http://www.google.com/finance/historical?q=GOOG&histperiod=daily&startdate=Apr+1+2014&enddate=Apr+15+2014&output=csv"
        self.base_url = "http://www.google.com/finance/historical?q={}&histperiod=daily&startdate={}&enddate={}&output=csv"
        self.cached_data = {}

    def fetch_stock_data(self, ticker, day, field):

        day_string = day.strftime("%d-%b-%y")

        if day > datetime.date.today():
            return None

        if not (ticker in self.cached_data and day_string in self.cached_data[ticker]):

            start_day = day
            end_day = day + relativedelta(years=1)

            if start_day > datetime.date.today():
                start_day = datetime.date.today()
            if end_day > datetime.date.today():
                end_day = datetime.date.today()

            start_day_string = start_day.strftime("%d+%b+%Y")
            end_day_string = end_day.strftime("%d+%b+%Y")
            url = self.base_url.format(ticker, start_day_string, end_day_string)
            print("FETCH: " + url)
            r = requests.get(url)
            lines = r.text.split("\n")
            data = []
            for l in lines:
                data.append(l.split(","))

            if ticker not in self.cached_data:
                self.cached_data[ticker] = {}

            header = data[0]

            for d in data[1:]:

                if len(d) < len(header):
                    continue

                self.cached_data[ticker][d[0]] = {}
                for i in range(1, len(header)):
                    self.cached_data[ticker][d[0]][header[i]] = d[i]

            for single_date in daterange(start_day, end_day):
                single_day_string = single_date.strftime("%d-%b-%y")
                if single_day_string not in self.cached_data[ticker]:
                    self.cached_data[ticker][single_day_string] = "Closed"

        if self.cached_data[ticker][day_string] == "Closed":
            return 0
        return self.cached_data[ticker][day_string][field]


def main():

    ticker = "GOOG"
    day = date(2018, 1, 1)
    field = "Open"

    sg = StockGrabber()

    n = sg.fetch_stock_data(ticker, day, field)
    print(ticker + " " + str(day) + " " + field + " " + str(n))

    day = date(2017, 1, 1)

    n = sg.fetch_stock_data(ticker, day, field)
    print(ticker + " " + str(day) + " " + field + " " + str(n))

    day = date(2017, 2, 10)

    n = sg.fetch_stock_data(ticker, day, field)
    print(ticker + " " + str(day) + " " + field + " " + str(n))






if __name__ == "__main__":
    main()