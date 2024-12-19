import mysql.connector as mydb
con=mydb.connect(host='localhost',
                 user='root',
                 password='password',
                 database='banking_system')
curr=con.cursor()
query="""CREATE TABLE USER(
         Name VARCHAR(50) NOT NULL,
         Account_Number VARCHAR(10) PRIMARY KEY,
         DOB DATE NOT NULL,
         City VARCHAR(20),
         Password VARCHAR(50),
         Initial_Balance DECIMAL(15,2) DEFAULT 2000.00,
         Contact_Number VARCHAR(10),
         Email_ID VARCHAR(100) UNIQUE,
         Address TEXT)"""
curr.execute(query)
