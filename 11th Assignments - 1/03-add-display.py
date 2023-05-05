#! /usr/bin/python3

def Add(n):
    with open('jvm.dat', 'a') as file:
        for i in range(n):
            line = input("Enter line " + str(i+1) + ": ")
            file.write(line + "\n")


n = int(input("Enter the number of lines: "))

def display():
    with open('jvm.dat', 'r') as file:
        content = file.read()
        content = content.replace(" ","#")
        print(content)

Add(n)
display()


# Output:
#
# Enter the number of lines: 3
# Enter line 1: This is line 1
# Enter line 2: This is line 2
# Enter line 3: This is line 3 4
# line#1
# line#2
# line#3#4
