import mysql.connector as abc
import tabulate
import random
con = abc.connect(host = "localhost", port = "3306", user = "root", passwd = "root", database = "project")
cur = con.cursor()
sno = 0
def add():
    global sno
    name = input("Enter name: ")
    regno = random.randint(10000, 99999)
    dob = input("Enter date(YYYY-MM-DD): ")
    sex = input("Enter sex: ")
    address = input("Enter address: ")
    sno=sno+1
    s = "insert into student values({},'{}',{},'{}','{}','{}')".format(sno, name, regno, dob, sex, address)
    print("Your regno is", regno)
    print("Record added")
    cur.execute(s)
    con.commit()

def edit(regno):
    name = input("Enter name: ")
    dob = input("Enter date(YYYY-MM-DD): ")
    sex = input("Enter sex: ")
    address = input("Enter address: ")
    s = "update student set name = '{}', dob = '{}', sex = '{}', address = '{}' where regno = {}".format(name, dob, sex, address, regno)
    cur.execute(s)
    con.commit()

def delete(regno):
    s = "delete from student where regno = {}".format(regno)
    cur.execute(s)
    if cur.rowcount == 0:
        print("No data")
    else:
        print("Record removed")
    con.commit()

def search(regno):
    s = "select regno, name, dob, sex, address from student where regno = {}".format(regno)
    cur.execute(s)
    data = cur.fetchall()
    hdr = ["Regno", "Name", "DOB", "Sex", "Address"]
    print(tabulate.tabulate(data, headers=hdr,tablefmt="outline"))
    if cur.rowcount == 0:
        print("Data not found")
    con.commit()

def display():
    s = "select * from student"
    cur.execute(s)
    data = cur.fetchall()
    hdr = ["S.No.", "Name", "Regno", "DOB", "Sex", "Address"]
    print("Displaying Student records...")
    print(tabulate.tabulate(data, headers=hdr,tablefmt="outline"))
    if cur.rowcount == 0:
        print("No data")
    con.commit()

def store_attendance(regno):
    name = input("Enter name: ")
    absent = int(input("Enter no. of days absent: "))
    leaves = int(input("Enter no. of leaves taken: "))
    tot_days = 200
    att = ((tot_days - (absent + leaves)) / tot_days) * 100
    s = "insert into attendance values({}, '{}', {}, {}, {}, {})".format(regno, name, absent, leaves, tot_days, att)
    cur.execute(s)
    print("Data stored")
    con.commit()

def show_attendance(regno):
    s = "select regno, name, days_absent, leaves, total_working_days, attendance from attendance"
    cur.execute(s)
    data = cur.fetchall()
    hdr = ["Regno", "Name", "Days Absent", "Leaves", "Total working days", "Attendance(%)"]
    print("Displaying Student Attendance Records...")
    print(tabulate.tabulate(data, headers=hdr,tablefmt="outline"))
    con.commit()

def marks_insertion(regno):
    name = input("Enter name: ")
    stream = input("Enter stream: ")
    if stream.upper() == "SCIENCE":
        sub1 = int(input("Enter physics marks: "))
        sub2 = int(input("Enter chemistry marks: "))
        sub3 = int(input("Enter maths/biology marks: "))
        sub4 = int(input("Enter CS/EG marks: "))
        sub5 = int(input("Enter english marks: "))
    elif stream.upper() == "COMMERCE":
        sub1 = int(input("Enter accountancy marks: "))
        sub2 = int(input("Enter BST marks: "))
        sub3 = int(input("Enter maths marks: "))
        sub4 = int(input("Enter economics marks: "))
        sub5 = int(input("Enter english marks: "))
    elif stream.upper() == "HUMANITIES":
        sub1 = int(input("Enter history marks: "))
        sub2 = int(input("Enter psychology marks: "))
        sub3 = int(input("Enter maths/pol. sci. marks: "))
        sub4 = int(input("Enter economics marks: "))
        sub5 = int(input("Enter english marks: "))
    agg = (sub1+sub2+sub3+sub4+sub5)/5
    if agg >= 33:
        result = "PASS"
    else:
        result = "FAIL"
    s = "insert into report values({},'{}','{}',{},{},{},{},{},{},'{}')".format(regno,name,stream,sub1,sub2,sub3,sub4,sub5,agg,result)
    print("Marks inserted")
    cur.execute(s)
    con.commit()

def report(regno):
    s = "select * from report"
    cur.execute(s)
    data = cur.fetchall()
    hdr = ["Regno", "Name", "Stream", "Sub1", "Sub2", "Sub3", "Sub4", "Sub5", "Sub6", "Aggregate", "Result"]
    print(tabulate.tabulate(data, headers=hdr, tablefmt="outline"))

ch = ""
us = input("Enter username: ")
pw = input("Enter password: ")
if pw.upper() == "ROOT" and us.upper() == "ROOT":
        print("Entry authorised!!\nWelcome to the STUDENT MANAGEMENT SOFTWARE!!")
        while ch != "9":
            print("\n1.Student Enrollment\n2.Edit\n3.Deletion\n4.Search\n5.Display Student details\n6.Store Attendance\n7.Show Attendance\n8.Insert marks\n9.Report\n10.Exit")
            ch = input("Select your option: ")
            if ch == "1":
                add()
            elif ch == "2":
                regno = int(input("Enter regno to edit: "))
                edit(regno)
            elif ch == "3":
                regno = int(input("Enter regno to delete: "))
                delete(regno)
            elif ch == "4":
                regno = int(input("Enter regno to search: "))
                search(regno)
            elif ch == "5":
                display()
            elif ch == "6":
                regno = int(input("Enter regno to store attendance: "))
                store_attendance(regno)
            elif ch == "7":
                regno = int(input("Enter regno to show attendance: "))
                show_attendance(regno)
            elif ch == "8":
                regno = int(input("Enter regno to insert marks: "))
                marks_insertion(regno)
            elif ch == "9":
                regno = int(input("Enter regno to show report: "))
                report(regno)
            elif ch == "10":
                print("Thank you!!")
else:
    print("Incorrect password/username")