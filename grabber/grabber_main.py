import datetime

from grabber.variables import Variables


def main():

    v = Variables()
    variables = v.get_variable_list()

    for variable in variables:
        print(variable['name'] + " " + str(variable['getter'](datetime.datetime.now())))


if __name__ == "__main__":
    main()
