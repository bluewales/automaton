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
    variables = v.get_variable_list()

    start_date = date(2017, 1, 1)
    end_date = datetime.date.today()

    for single_date in daterange(start_date, end_date):
        for variable in variables:
            day = single_date

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
