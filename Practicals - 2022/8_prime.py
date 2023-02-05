#! /usr/bin/python3

num = int(input("Enter the number: "))

fac=0
for i in range(1, num):
    if num%i==0:
        fac+=1

if fac > 1:
    print("Not a prime number.")
else:
    print("Prime Number.")
