# Udacity Log Analysis Project

<a href="https://www.udacity.com/">
  <img src="https://s3-us-west-1.amazonaws.com/udacity-content/rebrand/svg/logo.min.svg" width="300" alt="Udacity logo">
</a>

## Author
Denis Murphy

## Purpose of Project

Create a tool to analyse the data from a news website and find answers to the following 3 questions:

1. What are the most popular 3 articls of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

## Instructions

Install the latest version of [VirtualBox](https://www.virtualbox.org/wiki/Downloads).
Install the latest version of [Vagrant](https://www.vagrantup.com/).

Download Vagrantfile -- contains the settings for this project. </br>
Download newsdata.sql -- contains the data to create the PostgreSQL. </br> database with.

<a href="https://drive.google.com/uc?export=download&id=1H_FA_WJQ_cPILbi8mAKymbfnVEn6kU9p" download>Newsdata.sql</a></br>
<a href="https://drive.google.com/uc?export=download&id=1t0uXEVC2UIr8LRiCOkz24O4WUYUsgY4I" download>Vagrant file</a>


```
vagrant up
vagrant ssh
cd /vagrant
psql -d news -f newsdata.sql (run the sql statements to create the tables in the database)
psql -d news (whenever you need to connect to the news database)
\q - exits the database and the psql prompt

Run Log analysis tool using
python3 log_analysis.py

```

## Project Design

connect_to_db() function created to allow you to connect to the database and run SQL queries on the database from this function.

print_answers() function created to print the items in list of tuples underneath each other and with the correct formatting.

main() function created for the print_answers() function to take in the results from the sql queries ran from the connect_to_db function.

query variable used to pass in the sql queries 1, 2 and 3 to reuse the code.

print_percent() function created to return the answer to question 3 with the correct
formatting and to convert the date to the format displaying month name.


## Create Views
### Question 2

#### articlecount view
```
create articlecount view as select title, count(*) as views from articles join log on articles.slug = substring(log.path, 10) group by title order by views DESC;
```

#### authorname view

```
create view authorname as select name, title from authors, articles  where authors.id = articles.author;
```

### Question 3

#### totalrequests view

```
create view totalrequests as select cast(time as date), count(time) as totalrequests from log group by cast(time as date);

```

#### badrequests view

```
create view badrequests as select cast(time as date)as requesttimes, count(time) as badrequests from log where status not like '%200%' group by cast(time as date);

```


#### totalandbadrequests view

```
create view totalandbadrequests as select time, badrequests, totalrequests from totalrequests join badrequests on totalrequests.time = badrequests.requesttimes;

```

#### percentageerrors view

```
create view percentageerrors as select time, cast(cast(badrequests as float) / cast(totalrequests as float) * 100 as decimal(5,1)) as percent from totalandbadrequests;
```
