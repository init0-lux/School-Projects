#! /usr/bin/python3

n = int(input("Enter the value of n: "))

i=1
sum=0
sign=True
while i<=n*2:
    j=1
    fac=1

    while j<=i:
        fac*=j
        j=j+1

    if sign:
        sum+=fac
        sign=False
    else:
        sum-=fac
        sign=True

    i=i+1
print(sum)
