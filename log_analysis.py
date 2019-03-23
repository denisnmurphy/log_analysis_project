#!/usr/bin/python=3

import psycopg2

DBNAME = "news"

query_1 = """select title, count(*) as views from articles
             join log on articles.slug = substring(log.path, 10)
             group by title order by views DESC limit 3;"""

# query_2 =

# query_3 =

def connect_to_db():

    conn = psycopg2.connect(database=DBNAME)
    cursor = conn.cursor()
    cursor.execute(query_1)
    results = cursor.fetchall()
    conn.close
    return results




def print_answers(results):

    print('-------------')
    for result, view in results:
        print(result, '--', view)




def main():
    print_answers(connect_to_db())
main()
