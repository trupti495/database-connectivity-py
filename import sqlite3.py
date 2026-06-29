import sqlite3

con = sqlite3.connect("student.db")
cur = con.cursor()

cur.execute("INSERT INTO stud VALUES (11,'Rahul',20)")

con.commit()
con.close()