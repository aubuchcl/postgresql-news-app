import psycopg2

DBNAME = "news"
db = psycopg2.connect(database=DBNAME)

c = db.cursor()
# query = "select * from articles"
# c.execute(query)
# rows = c.fetchall()
#
# print("row data")
# print(rows)
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
             total desc;''')
test = c.fetchall()

print('test data')
print(test)
