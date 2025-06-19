import sqlite3 as sql
database= sql.connect('C:\SQLite\schooltest.db')
do= database.cursor()

print("Connected to the database successfully")

print("Insert value into student table")
stId=int(input("Enter Student ID(Note : Primary Key) :"))
stName=str(input("Enter Student Name: "))
stAge=int(input("Enter Student Age: "))
stMarks=int(input("Enter Student Marks: "))

try:
    do.execute("INSERT INTO student (StudentID, name, age, marks) VALUES (?, ?, ?, ?)", (stId, stName, stAge, stMarks))
    database.commit()
    print("Data inserted successfully")
except Exception as e:
    print("Error occurred:", e)

print("\n"*5)
print("Updated value in student table ....")
print("\n"*5)
print("Display all records from student table")
do.execute("SELECT * FROM student")
rows = do.fetchall()
for row in rows:
    print(row)