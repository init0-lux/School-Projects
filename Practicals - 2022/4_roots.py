#! /usr/bin/python3

a=int(input("Enter the value of a: "))
b=int(input("Enter the value of b: "))
c=int(input("Enter the value of c: "))

D = ( b**2 - 4*a*c ) ** 0.5

if D > 0:
    print("Roots are real and unequal")
elif D < 0:
    print("Roots are imaginary")
else:
    print("Roots are real and equal (0)")
