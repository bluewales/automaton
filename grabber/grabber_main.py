import datetime
from datetime import timedelta, date

from grabber.variables import Variables
from database import Database


def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)


def main():

    v = Variables()
    db = Database()

    start_date = date(2017, 6, 1)
    end_date = datetime.date.today()

    for variable in v.get_variable_list():
        for day in daterange(start_date, end_date):

            if db.value_exists(variable, day):
                continue

            value = variable['fetcher'](day)

            if value is None:
                print("Could not fetch " + variable['name'] + " for " + str(day))
                continue

            db.save_value(variable, value, day)

            print(variable['name'] + " " + str(day) + " " + str(value))


if __name__ == "__main__":
    main()
