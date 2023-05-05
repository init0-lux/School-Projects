#! /usr/bin/python3

import pickle

def add():
    with open("student.dat", "ab") as file:
        n = int(input("Enter the number of records to add: "))
        for i in range(n):
         
            name = input("Enter name of student: ")
            roll = int(input("Enter roll number: "))
            marks = float(input("Enter marks: "))
            student = {"name": name, "roll": roll, "marks": marks}
           
            pickle.dump(student, file)
            print()

def update():
    roll = int(input("Enter roll number to update marks: "))
   
    with open("student.dat", "rb") as file1, open("temp.dat", "wb") as file2:
        while True:
            try:
                student = pickle.load(file1)
                if student["roll"] == roll:
                    marks = float(input("Enter new marks: "))
                    student["marks"] = marks
                pickle.dump(student, file2)
            except EOFError:
                break
    
    with open("student.dat", "wb") as file1, open("temp.dat", "rb") as file2:
        while True:
            try:
                student = pickle.load(file2)
                pickle.dump(student, file1)
            except EOFError:
                break

def display():
    with open('student.dat', 'rb') as f:
        while True:
            try:
                student = pickle.load(f)
                print("Name:", student['name'])
                print("Roll no:", student['roll'])
                print("Marks:", student['marks'])
                print()
            except:
                break


add()
update()
display()


"""
Output: 

Enter the number of records to add: 3
Enter name of student: A
Enter roll number: 1
Enter marks: 10

Enter name of student: B
Enter roll number: 2
Enter marks: 20

Enter name of student: C
Enter roll number: 3
Enter marks: 30

Enter roll number to update marks: 2
Enter new marks: 40

Name: A
Roll no: 1
Marks: 10.0

Name: B
Roll no: 2
Marks: 40.0

Name: C
Roll no: 3
Marks: 30.0
"""
