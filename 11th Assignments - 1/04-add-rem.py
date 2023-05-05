#! /usr/bin/python3

def add(n):
    with open("input.txt", "a") as file:
        for i in range(n):
            line = input("Enter line " + str(i+1) + ": ")
            file.write(line + "\n")

def rem():
    out=[]
    with open("input.txt", "r") as inf:
        lines = inf.readlines()
        for line in lines:
            if "a" in line:
                out.append(line)

    with open("output.txt", 'a') as outf:
        for i in out:
            outf.write(i)

n = int(input("Enter the number of lines: "))

add(n)
rem()

# Output: 
# Enter the number of lines: 3
# Enter line 1: asdf
# Enter line 2: uuu
# Enter line 3: eee
# 
# output.txt contents:
# asdf
