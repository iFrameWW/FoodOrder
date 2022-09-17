import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='PROJ_WEB'
)

mcs = mydb.cursor()

# mcs.execute("CREATE DATABASE PROJ_WEB")

# mcs.execute("""CREATE TABLE Customers(
#     Customer_ID INT AUTO_INCREMENT PRIMARY KEY, 
#     Customer_Name VARCHAR(255), 
#     User VARCHAR(255), Password VARCHAR(255), 
#     Email VARCHAR(255), address text, Tel VARCHAR(10), 
#     Payment_Brand VARCHAR(255), Payment_ID VARCHAR(20), 
#     Payment_Holder_Name VARCHAR(255))""")

# mcs.execute("""CREATE TABLE Food_Menu(
#     Food_ID INT AUTO_INCREMENT PRIMARY KEY,
#     Food_Name VARCHAR(255),
#     Price FLOAT(7,2),
#     QTY_Stock INT,
#     Status INT(1))""")

# mcs.execute("""CREATE TABLE CATEGORIES(
#     CATAGORT_ID INT AUTO_INCREMENT PRIMARY KEY,
#     CATAGORY_NAME VARCHAR(255)    
#     )""")

# mcs.execute("""CREATE TABLE Order(
#     Order_ID INT AUTO_INCREMENT PRIMARY KEY,
      
# )
# """)