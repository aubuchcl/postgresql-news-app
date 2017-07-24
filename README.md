Vagrant setup was not working so the following command will work as
long as you have some type of db server application to run (I am using postico)

(from command line)
steps
1. psql
2. CREATE DATABASE news;
3. \i newsdata.sql
4. \d articles (to make sure articles db has properly populated)
5. \d authors and \d log for the others

this should have the database set up

