import requests


example_url = "http://www.google.com/finance/historical?q=GOOG&histperiod=daily&startdate=Apr+1+2014&enddate=Apr+15+2014&output=csv"

base_url = "http://www.google.com/finance/historical?q={}&histperiod=daily&startdate={}+{}+{}&enddate={}+{}+{}&output=csv"




def main():

    ticker = "GOOG"

    start_month = "Jan"
    start_day = 15
    start_year = 2017

    end_month = "Apr"
    end_day = 17
    end_year = 2017

    url = base_url.format(ticker, start_month, start_day, start_year, end_month, end_day, end_year)
    print(url)
    r = requests.get(url)
    print(r.text)


if __name__ == "__main__":
    main()