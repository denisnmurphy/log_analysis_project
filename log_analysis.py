#!/usr/bin/python=3

import psycopg2

DBNAME = "news"

# query_1 =

# query_2 =

# query_3 =

def connect_to_db():
    conn = psycopg2.connect(database=DBNAME)
    cursor = conn.cursor()
    cursor.execute("select * from articles")
    results = cursor.fetchall()
    print(results)
    conn.close
connect_to_db()
