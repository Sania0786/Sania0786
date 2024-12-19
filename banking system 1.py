import mysql.connector as mydb
con=mydb.connect(host='localhost',
                 user='root',
                 password='password')
curr=con.cursor()
curr.execute("CREATE DATABASE Banking_System")
