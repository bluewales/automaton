import MySQLdb
import json
import pandas as pd
import numpy as np

from flask import Flask
from flask import render_template
from subprocess import call
import os

from database import Database

app = Flask(__name__)





@app.route('/')
def hello_world(name=None):
    db = MySQLdb.connect(host="tradingseas.com", user="automaton", passwd="autopass", db="automaton")

    q = "select tag,type from dev_variables group by tag,type order by type,tag"
    cur = db.cursor()
    cur.execute(q)
    vars = []
    types = []
    for row in cur.fetchall():
        if row[1] not in types:
            types.append(row[1])
        vars.append(row)

    return render_template('variables.html', vars=vars, types=types)


@app.route('/stock/<tag>/data.csv')
def stock_data(tag):
    db = Database()
    q = "select tag, detail, day, value from dev_variables inner join dev_values on id=variable_id\
        where tag='{0}' and value>0 order by day".format(
        tag)
    df = db.query_to_df(q)
    df.columns = ['tag', 'detail', 'day', 'value']
    nw_df = df.pivot(index='day', columns='detail', values='value')
    return nw_df.to_csv()


def stock_page(tag):
    return render_template('stock_page.html', tag=tag)


def calendar_page(tag):
    return "not implemented"


@app.route('/<type>/<tag>')
def variable_page(type, tag):
    if type == "stock" :
        return stock_page(tag)
    elif type == "calendar":
        return calendar_page(tag)


@app.route('/test')
def test():
    return render_template('test.html')


@app.after_request
def response_minify(response):
    """
    minify html response to decrease site traffic
    """
    if response.content_type == u'text/html; charset=utf-8':
        # response.set_data(
        #    response.get_data(as_text=True).replace('\n',"")
        # )

        return response
    return response

if __name__ == '__main__':
    app.config['DEBUG'] = True
    app.run()