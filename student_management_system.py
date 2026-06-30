from reportlab.platypus import SimpleDocTemplate, Table
import sqlite3
import smtplib
from email.message import EmailMessage
con = sqlite3.connect("sms.db")
cur = con.cursor()

while True:

    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. Update Student")
    print("3. Read Student")
    print("4. Search Student")
    print("5. Delete Student")
    print("6. Result")
    print("7. Reports")
    print("8. download result")
    print("9. Exit")
   

    choice = int(input("Enter Choice : "))

    match choice:

        case 1:
            id = int(input("Enter ID : "))
            name = input("Enter Name : ")
            age = int(input("Enter Age : "))
            city = input("Enter City : ")
            java=int(input("enter java marks"))
            python=int(input("enter python marks"))
            cpp=int(input("enter cpp marks"))
            database=int(input("enter database marks"))
            total=int(input("enter total marks"))
            percentage=float(input("enter your percentage"))

            cur.execute("INSERT INTO student VALUES(?,?,?,?,?,?,?,?,?,?)",(id,name,age,city,java,python,cpp,database,total,percentage))
            con.commit()

            print("Student Added Successfully")

        case 2:
            print("\n1. Update Name")
            print("2. Update Age")
            print("3. Update City")
            print("4. Update Marks")
            print("5. update particular student data")
            print("6. update all student marks")
            ch = int(input("Enter Choice : "))
            

            match ch:
                case 1:
                    sid = int(input("Enter Student ID : "))
                    name = input("Enter New Name : ")
                    cur.execute(
                        "UPDATE student SET name=? WHERE id=?",
                        (name, sid)
                    )
                    con.commit()
                case 2:
                    sid = int(input("Enter Student ID : "))
                    age = int(input("Enter New Age : "))
                    cur.execute(
                        "UPDATE student SET age=? WHERE id=?",
                        (age, sid)
                    )
                    con.commit()

                case 3:
                    sid = int(input("Enter Student ID : "))
                    city = input("Enter New City : ")
                    cur.execute(
                        "UPDATE student SET city=? WHERE id=?",
                        (city, sid)
                    )
                    con.commit()
                case 4:
                    sid = int(input("Enter Student ID : "))
                    java = float(input("Enter New Marks : "))
                    cur.execute(
                        "UPDATE student SET java=? WHERE id=?",
                        (java, sid)
                    )
                    con.commit()

                case 5:
                  sid = int(input("Enter Student ID to Update: "))
    

                  name = input("Enter New Name: ")
                  age = int(input("Enter New Age: "))
                  city = input("Enter New City: ")

                  java = int(input("Enter Java Marks: "))
                  python = int(input("Enter Python Marks: "))
                  cpp = int(input("Enter C++ Marks: "))
                  database = int(input("Enter Database Marks: "))

                  total = java + python + cpp + database
                  percentage = total / 4
                  cur.execute("""
                    UPDATE student
                    SET name=?,
                     age=?,
                     city=?,
                     java=?,
                     python=?,
                     cpp=?,
                     database=?,
                     total=?,
                     percentage=?
                     WHERE id=?
                     """, (name, age, city, java, python, cpp, database, total, percentage, sid))

                  con.commit()
                  print("Student Record Updated Successfully")

                case 6:
                    cur.execute("UPDATE student SET java = 0")
                    con.commit()

                case _:
                    print("enter valid choice please !!!")
                

        case 3:
        
         cur.execute("select * from student")
         data=cur.fetchall()
         print("\nID\tNAME\t\tAGE\tCITY\tJAVA\tPYTHON\tCPP\tDATABASE\tTOTAL\tPERCENTAGE")

         for i in data:
          print(f"{i[0]}\t{i[1]}\t{i[2]}\t{i[3]}\t{i[4]}\t{i[5]}\t{i[6]}\t{i[7]}\t{i[8]}\t{i[9]}")

        case 4:

            print("\n1. Search By ID")
            print("2. Search By Name")

            ch = int(input("Enter Choice : "))

            match ch:

                case 1:
                    sid = int(input("Enter ID : "))

                    cur.execute(
                        "SELECT * FROM student WHERE id=?",
                        (sid,)
                    )

                    print(cur.fetchone())

                case 2:
                    name = input("Enter Name : ")

                    cur.execute(
                        "SELECT * FROM student WHERE name=?",
                        (name,)
                    )

                    for i in cur.fetchall():
                        print(i)

        case 5:

            print("\n1. Delete By ID")
            print("2. Delete All")

            ch = int(input("Enter Choice : "))

            match ch:

                case 1:
                   sid = int(input("Enter ID : "))

                   cur.execute(
                      "SELECT * FROM student WHERE id=?",
                     (sid,)
                    )

                   data = cur.fetchone()

                   if data:
                     cur.execute("DELETE FROM student WHERE id=?",(sid,))
                     con.commit()
                     print("Record Deleted")
                   else:
                    print("Student is not present")
                    

                case 2:
                    cur.execute(
                        "DELETE FROM student"
                    )

                    con.commit()

                    print("All Records Deleted")

        case 6:

            cur.execute("SELECT * FROM student")

            for i in cur.fetchall():
             result = "PASS" if i[9] >= 35 else "FAIL"
             print(i, result)

        case 7:

            print("\n1. Pass Students")
            print("2. Fail Students")

            ch = int(input("Enter Choice : "))

            match ch:

                case 1:
                    cur.execute(
                        "SELECT * FROM student WHERE percentage>=35"
                    )

                    for i in cur.fetchall():
                        print(i)

                case 2:
                    cur.execute(
                        "SELECT * FROM student WHERE percentage<35"
                    )

                    for i in cur.fetchall():
                        print(i)

        case 8:

         print("\n1. Download PDF")
         print("2. Send Result by Email")

         ch = int(input("Enter Choice : "))

         match ch:

          case 1:
              print("1.one student")
              print("2.all student")
              ch=int(input("enter choice:"))
              
              match ch:
                case 1:
                 sid=int(input("enter id:"))
                                       
                 
                 cur.execute("SELECT * FROM student where id=?",(sid,))
                 data = cur.fetchall()

                 pdf = SimpleDocTemplate("student_report.pdf")

                 table_data = [
                  ["ID", "NAME", "AGE", "CITY", "JAVA", "PYTHON", "CPP", "DATABASE", "TOTAL", "PERCENTAGE"]
                  ]

                 for row in data:
                      table_data.append(list(row))

                 table = Table(table_data)

                 elements = [table]

                 pdf.build(elements)

                 print("PDF Generated Successfully")
                case 2:
                   
                 
                 cur.execute("SELECT * FROM student")
                 data = cur.fetchall()

                 pdf = SimpleDocTemplate("student_all_report.pdf")

                 table_data = [
                  ["ID", "NAME", "AGE", "CITY", "JAVA", "PYTHON", "CPP", "DATABASE", "TOTAL", "PERCENTAGE"]
                  ]

                 for row in data:
                      table_data.append(list(row))

                 table = Table(table_data)

                 elements = [table]

                 pdf.build(elements)

                 print("PDF Generated Successfully")
               
          case 2:

                receiver_email = input("Enter Email: ")

                msg = EmailMessage()
                msg["Subject"] = "Student Result"
                msg["From"] = "yourgmail@gmail.com"
                msg["To"] = receiver_email

                msg.set_content("Student Result PDF Attached")

                with open("student_report.pdf", "rb") as f:
                    msg.add_attachment(
                        f.read(),
                        maintype="application",
                        subtype="pdf",
                        filename="student_report.pdf"
                    )

                server = smtplib.SMTP("smtp.gmail.com", 587)
                server.starttls()
                server.login(
                    "shitoletrupti6@gmail.com",
                    "gkgg kjfe enrl jdmm"
                      )
                server.send_message(msg)
                server.quit()

                print("Email Sent Successfully")

          case _:
             print("Invalid Choice")                

        case 9:
            con.close()
            print("Thank You")
            break

        case _:
            print("Invalid Choice")