import configparser
import os
import json
import datetime
import MySQLdb


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
                    "type varchar(32))".format(variable_table, )
            cursor.execute(query)

        # check that variable is in table
        cursor = self.cnx.cursor()
        query = "select id from {0} where name='{1}'".format(variable_table, variable['name'])
        cursor.execute(query)

        # if not insert it
        if cursor.rowcount < 1:
            cursor = self.cnx.cursor()
            query = "insert into {0} " \
                    "(name, description, type) " \
                    "values ('{1}','{2}','{3}')".format(variable_table, variable['name'], variable['description'],
                                                        variable['type'])
            cursor.execute(query)

            cursor = self.cnx.cursor()
            query = "select id from {0} where name='{1}'".format(variable_table, variable['name'])
            cursor.execute(query)

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
                "values ({1}, '{2}', {3}) " \
                "ON DUPLICATE KEY UPDATE value={3}".format(values_table, str(variable_id), str(day), str(value))
        cursor.execute(query)

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
                "where day = '{2}' and name = '{3}'".format(values_table, variable_table, str(day), variable['name'])

        cursor.execute(query)
        return cursor.rowcount > 0


def main():
    db = Database()
    v = {
        'name': "month",
        'description': "the month part of the date",
        'type': "calendar"
    }
    db.save_value(v, 12, datetime.date.today())

if __name__ == "__main__":
    main()