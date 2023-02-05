#! /usr/bin/python3

while True:

    print("Choose the calculation you want: \n")
    print("1. Volume of Sphere")
    print("2. Volume of Cube")
    print("3. Volume of Cylinder")
    print("4. Exit\n")

    ch = int(input("Choice: "))

    if ch == 1:
        r = int(input("Enter the radius: "))
        print("Volume of Sphere =", r*(4.0/3.0)*3.14159*r*r)

    elif ch == 2:
        l = int(input("Enter the length: "))
        print("Volume of Cube =", l**3)

    elif ch == 3:
        r = int(input("Enter the radius: "))
        h = int(input("Enter the height: "))

        print("Volume of Cylinder =", 3.14159*r*r*h )

    else:
        break;
