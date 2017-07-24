import psycopg2

DBNAME = "news"
db = psycopg2.connect(database=DBNAME)

c = db.cursor()

# example of db api
# query = "select * from articles"
# c.execute(query)
# rows = c.fetchall()
#
# print("row data")
# print(rows)

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

# print(pop_articles[0])
# print(pop_articles[0][0])
# print(pop_articles[0][1])
# print(pop_articles[0][2])
print('articles data')
for row in pop_articles:
    print ('{} - {} views'.format(row[0], row[2]))
