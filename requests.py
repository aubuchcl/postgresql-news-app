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

# execute actual query
c.execute('''select
             *, fail/(fail+success)::numeric*100 as failure_rate
             from
             successrate''')

failure_rate = c.fetchall()

print('failure rate')
print('{} -- {}'.format(failure_rate[0][0], failure_rate[0][3]))
