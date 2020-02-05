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
    results = sql_query(c, ''' SELECT * FROM report2 ''')
    print(results)
    msg = 'SELECT * FROM report2'
    return render_template('index.html', results=results, msg=msg)

def main():
    global conn, c

if __name__=='__main__':
    main()
    app.run(debug=True)