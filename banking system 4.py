import mysql.connector as mydb
con=mydb.connect(host='localhost',
                 user='root',
                 password='password',
                 database='banking_system')
curr=con.cursor()
query3="""CREATE TABLE Transaction(
          Account_Number VARCHAR(10),
          Initial_Balance DECIMAL(15,2) DEFAULT 2000.00,
          Final_Balance DECIMAL(15,2) DEFAULT 2000.00)"""
curr.execute(query3)
