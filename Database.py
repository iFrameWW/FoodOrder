import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='PROJ_WEB'
)

mcs = mydb.cursor()

# mcs.execute("CREATE DATABASE PROJ_WEB")

