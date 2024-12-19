import mysql.connector as mydb
con=mydb.connect(host='localhost',
                 user='root',
                 password='password',
                 database='banking_system')
curr=con.cursor()
query2="""CREATE TABLE Login(
          Account_Number VARCHAR(10),
          Password VARCHAR(50),
          Is_active BOOLEAN DEFAULT TRUE)"""
curr.execute(query2)
    
