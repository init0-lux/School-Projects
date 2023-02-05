#! /usr/bin/python3

n = int(input("Enter the value of n: "))

i=1
sum=0
while i<=n*2:
    if i%2 != 0:
        j=1
        fac=1

        while j<=i:
            fac*=j
            j=j+1

        sum+=fac

    i=i+1
print(sum)
