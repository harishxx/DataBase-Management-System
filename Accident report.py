from tabulate import tabulate
import mysql.connector

con = mysql.connector.connect(host="localhost", user="root", password="@Abcd123456", database="connector")

# def insert(name, gpa, dept):
#     res = con.cursor()
#     sql = "insert into student (ID, NAME, GPA, DEPT) VALUES (%s, %s, %s, %s)"
#     student = (id, name, gpa, dept)
#     res.execute(sql, student)
#     con.commit()
#     print("\t\tData insert success")

def insert(id, name, gpa, dept):
    res = con.cursor()
    sql = "insert into student (ID, NAME, GPA, DEPT) VALUES (%s, %s, %s, %s)"
    try:
        gpa = float(gpa)  # Convert gpa to float
    except ValueError:
        print("Invalid GPA value. Please enter a numeric value.")
        return
    student = (id, name, gpa, dept)
    res.execute(sql, student)
    con.commit()
    print("\t\tData insert success")

def update(name, gpa, dept, id):
    res = con.cursor()
    sql = "update student SET NAME = %s, GPA = %s, DEPT = %s WHERE id=%s"
    try:
        gpa = float(gpa)  # Convert gpa to float
    except ValueError:
        print("Invalid GPA value. Please enter a numeric value.")
        return
    student = (name, gpa, dept, id)
    res.execute(sql, student)
    con.commit()
    print("\t\tData updated successfully")

def select():
    res = con.cursor()
    sql = "select ID, NAME, GPA, DEPT FROM student"
    res.execute(sql)
    result = res.fetchall()
    print(tabulate(result, headers=["ID", "NAME", "GPA", "DEPT"]))

def select1(id, name, gpa, dept):
    res = con.cursor()
    sql = "select ID, NAME, GPA, DEPT FROM student WHERE ID = %s AND NAME = %s AND GPA = %s AND DEPT = %s"
    student = (id, name, gpa, dept)
    res.execute(sql, student)
    result = res.fetchone()
    if result is not None:
        print(tabulate([result], headers=["ID", "NAME", "GPA", "DEPT"]))
    else:
        print("------------------------------------------------------")
        print("No rows found in the database.")
        print("------------------------------------------------------")

def delete(id):
    res = con.cursor()
    sql = "delete FROM student WHERE ID = %s"
    student = (id,)
    res.execute(sql, student)
    con.commit()
    print("Record deleted successfully")

while True:
    print("------------This is the CRUD Management---------------")
    print("1. Insert Data")
    print("2. Update Data")
    print("3. Select Data")
    print("4. View particular Data")
    print("5. Delete Data")
    print("6. Exit")
    print("------------------------------------------------------")
    choice = int(input("Enter Your Choice: "))
    if choice == 1:
        id = input("Enter id: ")
        name = input("Enter Name: ")
        gpa = input("Enter gpa: ")
        dept = input("Enter Dept: ")
        insert(name, gpa, dept)
    elif choice == 2:
        id = input("Enter id: ")
        name = input("Enter Name: ")
        gpa = input("Enter gpa: ")
        dept = input("Enter dept: ")
        update(name, gpa,dept,id)
    elif choice == 3:
        select()
    elif choice == 4:
        id = input("Enter The Id to View: ")
        name = input("Enter Name: ")
        gpa = input("Enter gpa: ")
        dept = input("Enter Dept: ")
        select1(id, name, gpa, dept)
    elif choice == 5:
        id = input("Enter The Id to Delete: ")
        delete(id)
    elif choice == 6:
        break
    else:
        print("Invalid Selection. Please Try Again!")