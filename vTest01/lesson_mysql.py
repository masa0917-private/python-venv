import mysql.connector

# conn = mysql.connector.connect(
#     host='127.0.0.1',
#     port='3306',
#     user='root',
#     password='masaya1167'
#     )

# cursor = conn.cursor()

# cursor.execute(
#     'CREATE DATABASE test_mysql_database'
# )

# cursor.close()
# conn.close ()

conn = mysql.connector.connect(
    host='127.0.0.1',
    port='3306',
    user='root',
    password='masaya1167',
    database='test_mysql_database',
    )
cursor = conn.cursor()
# cursor.execute('CREATE TABLE persons('
#                'id int NOT NULL AUTO_INCREMENT,'
#                'name varchar(14) NOT NULL,'
#                'PRIMARY KEY(id))')

cursor.execute('INSERT INTO persons(name) values("Mike")')
conn.commit()

cursor.execute('SELECT * FROM persons')
for row in cursor:
    print(row)

conn.commit()
cursor.close()
conn.close ()
