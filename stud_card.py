# import sql
#create connecttion
#create obj of cursor
# use method of cursor
# creating and insertion related queries only here
import sqlite3

conn=sqlite3.connect("student.db")

cursor=conn.cursor()

#table creation
cursor.execute('''
      create table if not exists stud(
               sid integer primary key,
               name text not null,
               age integer null)         
               ''')

print("created")

#insert
#cursor.execute("insert into stud(sid,name,age) values(?,?,?)",(1,"ram",21))
#conn.commit()
#print("data inserted")

sid=int(input("enter yr id:"))
name=input("enter yr name:")
age=int(input("enter yr age:"))
cursor.execute("insert into stud values(?,?,?)",(sid,name,age))
conn.commit()
print("data inserted")