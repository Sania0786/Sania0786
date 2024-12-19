#main
import mysql.connector as mydb
import random
con=mydb.connect(host='localhost',
                 user='root',
                 password='password',
                 database='banking_system')
curr=con.cursor()
def generate_account_number():
    return str(random.randint(1000000000, 9999999999))
def adduser():
    name=input("Enter your name:")
    dob=input("Enter date of birth(YYYY-MM-DD):")
    city=input("Enter city:")
    password=input("Enter password:")
    initial_balance = float(input("Enter Initial Balance (Minimum 2000): "))
    while initial_balance < 2000:
        print("Initial balance should be at least 2000.")
        initial_balance = float(input("Enter Initial Balance: "))
    contact=input("Enter contact no.:")
    email=input("Enter emailid:")
    address=input("Enter address:")
    account_number = generate_account_number()
    query="""INSERT INTO User(Name,Account_Number,DOB,City,Password,Initial_Balance,Contact_Number,Email_ID,Address)
             VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
    val=(name,account_number,dob,city,password,initial_balance,contact,email,address)
    curr.execute(query,val)
    query2="""INSERT INTO login(Account_Number,Password) VALUES(%s,%s)"""
    val2=(account_number,password)
    curr.execute(query2,val2)
    query3="""INSERT INTO transaction(Account_Number,Initial_Balance,Final_Balance) VALUES(%s,%s,%s)"""
    val3=(account_number,initial_balance,initial_balance)
    curr.execute(query3,val3)
    con.commit()
    print(f"User created successfully with account number: {account_number}")
def showuser():
    accountno=input("Enter your account no.:")
    query="""SELECT Name,Account_Number,DOB,City,Initial_Balance,Contact_Number,Email_ID,Address
             FROM User WHERE Account_Number=%s"""
    curr.execute(query,(accountno,))
    data=curr.fetchone()
    if data:
        print(f"Name:{data[0]}")
        print(f"Account Number:{data[1]}")
        print(f"DOB:{data[2]}")
        print(f"City:{data[3]}")
        print(f"Initial Balance:{data[4]}")
        print(f"Contact Number:{data[5]}")
        print(f"Email ID:{data[6]}")
        print(f"Address:{data[7]}")
    else:
        print("User not found")
def login():
    accountno=input("Enter account no.:")
    password=input("Enter password:")
    fetch="""SELECT Password FROM Login WHERE Account_Number=%s"""
    curr.execute(fetch,(accountno,))
    data=curr.fetchone()
    if data:
        if data[0]==password:
            ch=int(input("""Enter Your Choice:
                     1.Show Balance
                     2.Show transaction
                     3.Credit Amount
                     4.Debit amount
                     5.Active/Deactive account
                     6.change password
                     7.Update profile\n"""))
            if ch==1:
                query1="""SELECT Final_Balance FROM transaction WHERE Account_Number=%s"""
                curr.execute(query1,(accountno,))
                req1=curr.fetchone()
                print(f"Balance:{req1[0]}")
            elif ch==2:
                query2="""SELECT * FROM transaction WHERE Account_Number=%s"""
                curr.execute(query2,(accountno,))
                req2=curr.fetchone()
                print(f"Account Number:{req2[0]}")
                print(f"Initial Balance:{req2[1]}")
                print(f"Final balance:{req2[2]}")
            elif ch==3:
                amount=float(input("Enter amount to be credited:"))
                query3="""UPDATE transaction SET Final_Balance=Final_Balance+%s WHERE Account_Number=%s"""
                val=(amount,accountno)
                curr.execute(query3,val)
                con.commit()
                print(f'{amount} credited successfully')
            elif ch==4:
                amount=float(input("Enter amount to be debited:"))
                if amount<=2000.00:
                    query3="""UPDATE transaction SET Final_Balance=Final_Balance-%s WHERE Account_Number=%s"""
                    val=(amount,accountno)
                    curr.execute(query3,val)
                    con.commit()
                    print(f'{amount} debited successfully')
                else:
                    print("Wrong amount:")
            elif ch==5:
                query1="""SELECT Is_active FROM login WHERE Account_Number=%s"""
                curr.execute(query1,(accountno,))
                val=curr.fetchone()
                current=not val[0]
                query2="""UPDATE login SET Is_active=%s WHERE Account_Number=%s"""
                data=(current,accountno)
                curr.execute(query2,data)
                con.commit()
                if current:
                    print("Status: Active")
                else:
                    print("Status: Deactive")
            elif ch==6:
                pwd=input("Enter new password")
                query7="""UPDATE user SET Password=%s WHERE Account_Number=%s"""
                query8="""UPDATE login SET Password=%s WHERE Account_Number=%s"""
                val5=(pwd,accountno)
                curr.execute(query7,val5)
                curr.execute(query8,val5)
                con.commit()
                print("Password updated successfully")
            elif ch==7:
                newnm=input("Enter name:")
                newdob=input("Enter date of birth(YYYY-MM-DD):")
                newcity=input("Enter city:")
                newcontact=input("Enter contact no.:")
                newemail=input("Enter emailid:")
                newaddress=input("Enter address:")
                query="""UPDATE user SET Name=%s,DOB=%s,City=%s,Contact_Number=%s,Email_ID=%s,Address=%s WHERE
                         Account_Number=%s"""
                data=(newnm,newdob,newcity,newcontact,newemail,newaddress,accountno)
                curr.execute(query,data)
                con.commit()
                print("Profile updated successfully")
            else:
                print("Wrong choice")
        else:
            print("Wrong password")
    else:
        print("Wrong Account no.")
while True:
    ch=int(input("""Enter choice:
             1.Add User
             2.Show User
             3.Login
             4.Exit\n"""))
    if ch==1:
           adduser()
    elif ch==2:
        showuser()
    elif ch==3:
        login()
    elif ch==4:
        exit()
        break
    else:
        print("wrong choice")
        break
        
    
