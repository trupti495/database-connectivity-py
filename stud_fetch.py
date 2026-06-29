# fetching and updation
import sqlite3

conn=sqlite3.connect("student.db")

cursor=conn.cursor()

# fetch all
cursor.execute("select* from stud")
row=cursor.fetchall()
for i in row:
    print(i)

# fetch one 
sid=int(input("enter yr id:"))
cursor.execute("select * from stud where sid=?",(sid,))
row=cursor.fetchone()
print(row)

# update
#cursor.execute("update stud set name=? where sid=?",("tejas",1))
#conn.commit()
#print("update successfully")

# update from user input
sid=int(input("enter yr id:"))
cursor.execute("select * from stud where sid=?",(sid,))
row=cursor.fetchone()
print(row)
if sid==row[0]:
    newname=input("enter newname:")
    cursor.execute("update stud set name=? where sid=?",(newname,sid))
    conn.commit()
    print("data update")
else:
    print("no record found")   


