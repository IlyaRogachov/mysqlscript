include mysql-library
from getpass import getpass
from mysql.connector import connect, Error

try:
    with connect(
        host="192.168.56.104",
        user="ilya",
        password="rognarock",
        database="ilyadb",
    ) 
