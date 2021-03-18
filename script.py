include mysql-library
from getpass import getpass
from mysql.connector import connect, Error

try:
    with connect(
        host="192.168.56.104",
        user="ilya",
        password="rognarock",
        database="ilyadb",
    ) as connection:
        show_db_query = "SHOW DATABASES"
        with connection.cursor() as cursor:
            cursor.execute(show_db_query)
            for db in cursor:
                   print(db)
except Error as e:
    print(e) 

privet VOVA
