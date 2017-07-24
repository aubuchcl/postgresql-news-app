import psycopg2

DBNAME = "news"
db = psycopg2.connect(database=DBNAME)

c = db.cursor()

# articles query and sort

articles = '''select 
             title, path, count(path) as visits 
             from articles, log 
             where log.path = CONCAT('/article/', articles.slug) 
             group by 
             path, title 
             order by 
             visits desc limit 3;'''
c.execute(articles)

pop_articles = c.fetchall()

print('articles data')
for row in pop_articles:
    print ('{} - {} views'.format(row[0], row[2]))


# author sort and query
visitview = '''create view visitview as
             select
             name, author, title, path, count(path) as visits
             from articles, log, authors
             where log.path = CONCAT('/article/', articles.slug) and
             articles.author = authors.id
             group by
             path, title, name, author
             order by visits desc;'''

c.execute(visitview)
c.execute('''select 
             name, sum(visits) as total 
             from visitview 
             group by 
             name 
             order by 
             total desc limit 3;''')
authors = c.fetchall()

print('author data')

for row in authors:
    print('{} -- {} views'.format(row[0], row[1]))


# request success rate query and sort
successrate = '''CREATE VIEW successrate AS 
                 SELECT
                 time::date,
                 SUM(
                     CASE
                     WHEN status = '200 OK' THEN
                     1
                     ELSE
                     0
                     END
                     ) AS success,
                 SUM(
                    CASE
                    WHEN status = '404 NOT FOUND' THEN
                    1
                    ELSE
                    0
                    END
                    ) AS fail
                FROM
                log 
                group by 
                time::date;'''

c.execute(successrate)


c.execute('''select
             *, to_char(time, 'Mon DD, YYYY'), ROUND(fail/(fail+success)::numeric*100,2) as failure_rate
             from
             successrate
             ''')





failure_rate = c.fetchall()

print('failure rate')


for row in failure_rate:
    if int(row[4]) > 1:
        print('{} -- {}% errors'.format(row[3], row[4]))