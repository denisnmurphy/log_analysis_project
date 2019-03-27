#!/usr/bin/python=3

import psycopg2

DBNAME = "news"

query_1 = """select title, count(*) as views from articles
             join log on articles.slug = substring(log.path, 10)
             group by title order by views DESC limit 3;"""

query_2 = """select name, sum(views) as totalviews from authorname,
            articlecount where  authorname.title = articlecount.title
            group by authorname.name order by totalviews desc;"""


query_3 = """ select time, percent from percentageerrors
                where percent > 1.0;"""


def connect_to_db(query):

    conn = psycopg2.connect(database=DBNAME)
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close
    return results


def print_answers(results):

    print('-------------')
    for result, view in results:
        print(result, '--', view, 'views')


def print_percent(results):

    print('-------------')
    for result, view in results:
        date_time = result.strftime('%b %d, %Y')
        print(date_time, '--', view, '%', 'errors')


def main():

    print_answers(connect_to_db(query_1))
    print_answers(connect_to_db(query_2))
    print_percent(connect_to_db(query_3))


main()
