import mysql.connector


dataBase=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='Aditya.2006'
)


# making a cursor
cursorObject=dataBase.cursor()


# create database
# cursorObject.execute("CREATE DATABASE AddyCorp")

print("all done")