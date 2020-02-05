from flask import Flask, render_template, request, session, jsonify
import urllib.request
from datetime import datetime
import httpagentparser
import json
import os
import hashlib
from dbsetup import create_connection, sql_query

app = Flask(__name__)
app.secret_key = os.urandom(24)

database = "./pythonsqlite.db"
conn = create_connection(database)
c = conn.cursor()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/reports1')
def reportsIND():
    results = sql_query(c, ''' SELECT * FROM report1 ''')
    msg = 'SELECT * FROM report1'
    return render_template('reportsIND.html', results=results, msg=msg)

@app.route('/reports2')
def reportsUS():
    results = sql_query(c, ''' SELECT * FROM report2 ''')
    msg = 'SELECT * FROM report2'
    return render_template('reportsUS.html', results=results, msg=msg)

def main():
    global conn, c

if __name__=='__main__':
    main()
    app.run(debug=True)