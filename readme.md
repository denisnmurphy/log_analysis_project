# Udacity Log Analysis Project

<a href="https://www.udacity.com/">
  <img src="https://s3-us-west-1.amazonaws.com/udacity-content/rebrand/svg/logo.min.svg" width="300" alt="Udacity logo">
</a>

# Author
Denis Murphy

# Purpose of Project

Create a tool to analyse the data from a news website and find answers to the following 3 questions:

1. What are the most popular 3 articls of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

# Instructions

Install the latest version of VirtualBox.
Install the latest version of Vagrant

Download Vagranfile which contains the settings for this project.
Download newsdata.sql which contains the data to create the PostgreSQL database with.


```
vagrant up
vagrant ssh
cd /vagrant
psql -d news -f newsdata.sql (run the sql statements to create the tables in the database)
psql -d news (connect to the news database)


```

# Project Design

connect_to_db function created to allow you to connect to the database and run SQL queries on the database from this function.
