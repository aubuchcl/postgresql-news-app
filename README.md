Vagrant setup was not working so the following command will work as
long as you have some type of db server application to run (I am using postico)
here is the link the the lesson that has the newsdata.zip
https://classroom.udacity.com/nanodegrees/nd004-connect/parts/52f50785-064e-4221-9227-e5c076a840d0/modules/bc51d967-cb21-46f4-90ea-caf73439dc59/lessons/262a84d7-86dc-487d-98f9-648aa7ca5a0f/concepts/a9cf98c8-0325-4c68-b972-58d5957f1a91
I would have added the newsdata.sql file but git would not allow a file of this
size and the large file system I researched would not work
(from command line)
steps
1. psql
2. CREATE DATABASE news;
3. \i newsdata.sql
4. \d articles (to make sure articles db has properly populated)
5. \d authors and \d log for the others

this should have the database set up

from this point please run each file as follows

- from the command line and inside the directory you have cloned these files into:
-- run each file as so:  python 'filename'

if you would like to run all queries at once you can run python all_files.py