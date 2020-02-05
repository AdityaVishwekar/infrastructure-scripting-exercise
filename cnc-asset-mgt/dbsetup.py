import sqlite3
from sqlite3 import Error
import pandas as pd

def create_connection(database):
    try:
        conn = sqlite3.connect(database, isolation_level=None, check_same_thread = False)
        conn.row_factory = lambda c, r: dict(zip([col[0] for col in c.description], r))
        return conn
    except Error as e:
        print(e)

def create_table(c,sql):
    c.execute(sql)

def sql_query(c,sql):
    c.execute(sql)
    rows = c.fetchall()
    return rows

def load_Data(conn, table, data_url):
    data_table = pd.read_excel(data_url)
    data_table.to_sql(table, conn, dtype={
        'COMPANY' : 'varchar(225)',
        'Total Cash' : 'float',
        'Total Debt' : 'float',
        'Ratio' : 'float',
    } )

def main():
    database = "./pythonsqlite.db"

    # create a database connection
    conn = create_connection(database)
    if conn is not None:
        # create tables and load data from excel
        data_url = '../Reports/DebtRatioReport_IN_2020-02-04.xlsx'
        load_Data(conn, 'report1', data_url)
        data_url = '../Reports/DebtRatioReport_US_2020-02-05.xlsx'
        load_Data(conn, 'report2', data_url)
        print("Connection established!")
    else:
        print("Could not establish connection")
    

if __name__ == '__main__':
    main()