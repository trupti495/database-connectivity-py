# insert 5 record and and fetch record of student whose age 
# is a 18 and 25
import sqlite3

conn=sqlite3.connect("student.db")
cursor=conn.cursor()

records = [
    (3, "Rahul", 18),
    (4, "Priya", 20),
    (5, "Amit", 25),
    (6, "Sneha", 27),
    (7, "Rohan", 22)
]

cursor.executemany("INSERT INTO stud VALUES (?, ?, ?)", records)

cursor.execute("select name from stud where age between 18 and 25")
row=cursor.fetchall()
print(row)