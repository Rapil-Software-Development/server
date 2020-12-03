import pymysql.cursors

# Підключення до бази даних.
connection = pymysql.connect(host='localhost',
                             user='Yura',
                             password='',
                             db='complab',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

print("connect successful!!")


