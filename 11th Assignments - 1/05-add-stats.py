#! /usr/bin/python3

def add(n):
    with open('input.stats', 'a') as file:
        for i in range(n):
            line = input("Enter line " + str(i+1) + ": ")
            file.write(line)

def count():
    (vowel, upper, lower, digit, blank) = (0, 0, 0, 0, 0)
    with open('input.stats', 'r') as file:
        lines = file.read()
        for i in lines:
            if i in "aeiouAEIOU":
                vowel += 1
            if i.isupper():
                upper += 1
            if i.islower():
                lower += 1
            if i.isdigit():
                digit += 1
            if i.isspace():
                blank += 1

    print("Vowels = ", vowel, "\nUppercase = ", upper, "\nLowercase = ", lower, "\nDigits = ", digit, "\nBlankspaces = ", blank)

n = int(input("Enter the number of lines: "))

add(n)
count()

"""
Output: 

Enter the number of lines: 3
Enter line 1: This is a line
Enter line 2: 44
Enter line 3: AA3
Vowels =  7
Uppercase =  3
Lowercase =  10
Digits =  3
Blankspaces =  3
"""
