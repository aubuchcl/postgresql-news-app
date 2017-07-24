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
# c.execute('''select
#              *, ROUND(fail/(fail+success)::numeric*100,2) as failure_rate
#              from
#              successrate
#              ''')
c.execute('''select
             *, to_char(time, 'Mon DD, YYYY'), ROUND(fail/(fail+success)::numeric*100,2) as failure_rate
             from
             successrate
             ''')





failure_rate = c.fetchall()

print('failure rate')
# print(failure_rate)
# print('{} -- {}'.format(failure_rate[0][0], failure_rate[0][3]))

for row in failure_rate:
    if int(row[4]) > 1:
        print('{} -- {}% errors'.format(row[3], row[4]))

