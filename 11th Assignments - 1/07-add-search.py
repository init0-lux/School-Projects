#! /usr/bin/python3

import pickle

def add():
    n = int(input("Enter the number of records to be added: "))
    with open("student.dat", "ab") as f:
        for i in range(n):
            name = input("Enter the name of the student: ")
            roll = int(input("Enter the roll number of the student: "))
            pickle.dump((name, roll), f)

            print()

def search():
    roll = int(input("Enter the roll number to search: "))
    found = False
    with open("student.dat", "rb") as f:
        while True:
            try:
                name, r = pickle.load(f)
                if r == roll:
                    print("Name of the student with roll number", roll, "is", name)
                    found = True
                    break
            except:
                break
    if not found:
        print("No student found with roll number", roll)


add()
search()

"""
Output: 


Enter the number of records to be added: 2

Enter the name of the student: A
Enter the roll number of the student: 33

Enter the name of the student: b
Enter the roll number of the student: 39

Enter the roll number to search: 39
Name of the student with roll number 39 is b
"""
