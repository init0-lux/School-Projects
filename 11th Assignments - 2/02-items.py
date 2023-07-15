import csv

def Add():
    number = int(input("Enter the number of items to add: "))
    print()
    data = []
    
    for i in range(number):
        nm = input("Enter the name for item #"+str(i+1)+": ")
        pr = int(input("Enter the price of item #"+str(i+1)+": "))
        qt = int(input("Enter the quantity of item #"+str(i+1)+": "))
        print()
        
        data.append([i+1, nm, pr, qt])
    
    with open("items.csv", 'a') as csvfile:
        csvf = csv.writer(csvfile)
        csvf.writerows(data)

    Menu()

def Display():
    data = []

    with open("items.csv", 'r') as csvfile:
        csvf = csv.reader(csvfile)
        
        for row in csvf:
            if int(row[3]) < 10:
                data.append(row)

    print("Name#\t\tPrice#")
    for i in data:
        print(i[1], "\t\t", i[2]) 

    Menu()

def Search():
    data = []
    
    with open("items.csv", 'r') as csvfile:
        csvf = csv.reader(csvfile)
        
        for i in csvf:
            data.append(i)

    item = int(input("Enter the item no. to search for: "))
    
    found = False
    for i in data:
        if item == int(i[0]):
            print("Name =", i[1])
            found = True

    if not found:
        print("Error! Item does not exist!")

    Menu()

def Menu():
    print("\nWhat do you want?\n")
    print("1. Add items\n2. Display\n3. Search\n4. Quit\n")

    ch = int(input("Enter your Choice: "))

    if ch == 1:
        Add()

    elif ch == 2:
        Display()

    elif ch == 3:
        Search() 

    else:
        print("\nSorry to see you go!")
        exit()

Menu()
