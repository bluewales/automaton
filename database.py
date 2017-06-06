import configparser
import os
import json
import datetime
import MySQLdb

from grabber.variables import Variables


class Database:

    def __init__(self):
        config_file_path = os.path.join(os.path.dirname(__file__), "config.txt")
        self.config = configparser.ConfigParser()
        self.config.read(config_file_path)

        self.cnx = MySQLdb.connect(
            host=self.config['DATABASE']['servername'],
            user=self.config['DATABASE']['username'],
            password=self.config['DATABASE']['password'],
            database=self.config['DATABASE']['database'],
            use_unicode=True,
            charset="utf8"
        )

    def save_value(self, variable, value, day):

        variable_table = self.config['DATABASE']['table_prefix'] + "variables"
        values_table = self.config['DATABASE']['table_prefix'] + "values"

        # check that variable table exists
        cursor = self.cnx.cursor()
        cursor.execute("show tables")
        tables = [i[0] for i in cursor]

        # if not, create it
        if variable_table not in tables:
            cursor = self.cnx.cursor()
            query = "create table {0} " \
                    "(id int unsigned auto_increment primary key, " \
                    "name varchar(16), " \
                    "description varchar(128), " \
                    "type varchar(32))".format(variable_table)
            cursor.execute(query)

        # check that variable is in table
        cursor = self.cnx.cursor()
        query = "select id from {0} where name=%s".format(variable_table)

        cursor.execute(query, (variable['name'],))

        # if not insert it
        if cursor.rowcount < 1:
            cursor = self.cnx.cursor()
            query = "insert into {0} (name, description, type) values (%s, %s, %s)".format(variable_table)
            cursor.execute(query, (variable['name'], variable['description'], variable['type']))

            cursor = self.cnx.cursor()
            query = "select id from {0} where name=%s".format(variable_table)
            cursor.execute(query, (variable['name'],))

        # get variable id
        variable_id = [i[0] for i in cursor][0]

        # check that values table exists
        # if not create it
        if values_table not in tables:
            cursor = self.cnx.cursor()
            query = "create table {0} " \
                    "(variable_id int, day date, value double,  primary key (variable_id, day))".format(values_table)
            cursor.execute(query)

        # insert value, variable id, date into values table
        cursor = self.cnx.cursor()
        query = "insert into {0} " \
                "(variable_id, day, value) " \
                "values (%s, %s, %s) " \
                "ON DUPLICATE KEY UPDATE value=%s".format(values_table)
        cursor.execute(query, (str(variable_id), str(day), str(value), str(value)))

    def value_exists(self, variable, day):

        variable_table = self.config['DATABASE']['table_prefix'] + "variables"
        values_table = self.config['DATABASE']['table_prefix'] + "values"


        # check that the tables exist
        cursor = self.cnx.cursor()
        cursor.execute("show tables")
        tables = [i[0] for i in cursor]

        # if not, then we can't look for data
        if variable_table not in tables or values_table not in tables:
            return False

        cursor = self.cnx.cursor()
        query = "select value from " \
                "{0} inner join {1} on dev_values.variable_id = dev_variables.id " \
                "where day = %s and name = %s".format(values_table, variable_table)

        cursor.execute(query, (str(day), variable['name']))
        return cursor.rowcount > 0

    def load_values(self):
        variable_table = self.config['DATABASE']['table_prefix'] + "variables"
        values_table = self.config['DATABASE']['table_prefix'] + "values"

        # check that the tables exist
        cursor = self.cnx.cursor()
        cursor.execute("select day,name,value from dev_values inner join dev_variables on id=variable_id")

        data = {'min_date':datetime.date.today(), 'max_date':datetime.date(1970, 1, 1), 'values':{}, 'sums':{}, 'names':[]}
        for row in cursor:
            if row[0] not in data['values']:
                data['values'][row[0]] = {}
            data['values'][row[0]][row[1]] = row[2]

            if row[1] not in data['sums']:
                data['sums'][row[1]] = 0
            data['sums'][row[1]] += row[2]

            if row[1] not in data['names']:
                data['names'].append(row[1])

            if row[0] < data['min_date']:
                data['min_date'] = row[0]
            if row[0] > data['max_date']:
                data['max_date'] = row[0]

        data['avg'] = {}
        for name in data['names']:
            data['avg'][name] = data['sums'][name] / len(data['values'])

        print(data)
        return data


def main():
    db = Database()
    v = Variables().get_variable_list()[0]
    day = datetime.date.today()
    #db.save_value(v, v['fetcher'](day), day)
    db.load_values()

if __name__ == "__main__":
    main()