#! /usr/bin/python3

def add(n):
    with open('jvm.dat', 'a') as f:
        for i in range(n):
            line = input("Enter line " + str(i+1) + ": ")
            f.write(line + "\n")

def display():
    count = 0
    with open('jvm.dat', 'r') as f:
        content = f.readlines()
    lines = content

    for line in lines:
        if line[0] in "aeiouAEIOU":
            count+=1
            print(line)
    print("Number of lines starting with a vowel: ", count)

add(3)
display()

# Output:
#
# Enter line 1: aaaaaa
# Enter line 2: asfdasdf
# Enter line 3: bbcjk
# 
# aaaaaa
# asfdasdf
# Number of lines starting with a vowel: 2
