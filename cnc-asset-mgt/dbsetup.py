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

def main():
    database = "./pythonsqlite.db"
    sql_create_report = """ 
            CREATE TABLE IF NOT EXISTS report (
                company varchar(225) NOT NULL,
                total_cash float,
                total_debt float,
                ratio float
            ); 
        """

    # create a database connection
    conn = create_connection(database)
    if conn is not None:
        # create tables
        create_table(conn, sql_create_report)
        print("Connection established!")
    else:
        print("Could not establish connection")
    
    # load data from excel
    data_url = '../Reports/DebtRatioReport_IN_2020-02-04.xlsx'
    data_table = pd.read_excel(data_url)
    
    # data_table.to_sql('report1', conn, dtype={
    #     'COMPANY' : 'varchar(225)',
    #     'Total Cash' : 'float',
    #     'Total Debt' : 'float',
    #     'Ratio' : 'float',
    # } )

    data_url = '../Reports/DebtRatioReport_US_2020-02-05.xlsx'
    data_table = pd.read_excel(data_url)
    
    data_table.to_sql('report2', conn, dtype={
        'COMPANY' : 'varchar(225)',
        'Total Cash' : 'float',
        'Total Debt' : 'float',
        'Ratio' : 'float',
    } )

if __name__ == '__main__':
    main()