#! /usr/bin/python3

import os
import pickle

def add(n):
    with open('items.dat', 'ab') as f:
        for i in range(n):
            item_num = int(input("Enter item number: "))
            item_name = input("Enter item name: ")
            unit_price = float(input("Enter unit price: "))
            quantity = int(input("Enter quantity: "))
            
            item = [item_num, item_name, unit_price, quantity]
            pickle.dump(item, f)
            print()

def display():
    with open('items.dat', 'rb') as f:
        try:
            while True:
                item = pickle.load(f)
                print("Item Number: ", item[0])
                print("Item Name: ", item[1])
                print("Unit Price: ", item[2])
                print("Quantity: ", item[3])
                print("----------------------------")
                print()
        except:
            pass

def search():
    total_value = 0
    total_quantity = 0
    with open('items.dat', 'rb') as f:
        try:
            while True:
                item = pickle.load(f)
                if item[2] > 100:
                    total_value += item[2] * item[3]
                    total_quantity += item[3]
        except:
            pass
    print("Total value of items with quantity > 100: ", total_value)
    print("Total quantity of items with quantity > 100: ", total_quantity)
    print()

def update():
    item_num = int(input("Enter item number to update: "))
    found = False
    with open('items.dat', 'rb') as f1, open('temp.dat', 'wb') as f2:
        try:
            while True:
                item = pickle.load(f1)
                if item[0] == item_num:
                    found = True
                    item[2] = float(input("Enter new unit price: "))
                    item[3] = int(input("Enter new quantity: "))
                pickle.dump(item, f2)
        except:
            pass
    if found:
        os.remove('items.dat')
        os.rename('temp.dat', 'items.dat')
        print("Item updated successfully!")
    else:
        print("Item not found!")

    print()

def delete():
    with open('items.dat', 'rb') as f1, open('temp.dat', 'wb') as f2:
        try:
            while True:
                item = pickle.load(f1)
                if item[3] != 0:
                    pickle.dump(item, f2)
        except:
            pass
    os.remove('items.dat')
    os.rename('temp.dat', 'items.dat')
    print("Items with quantity 0 deleted successfully!\n")

def menu():
    while True:
        print("Menu:\n")
        print("1. Add items")
        print("2. Display all items")
        print("3. Search for items with quantity > 100")
        print("4. Update item's unit price and quantity")
        print("5. Delete items with quantity 0")
        print("6. Quit\n")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            n = int(input("Enter the number of items to add: "))
            add(n)
        elif choice == 2:
            display()
        elif choice == 3:
            search()
        elif choice == 4:
            update()
        elif choice == 5:
            delete()
        elif choice == 6:
            exit()
        else:
            print("Invalid Choice")


menu()

"""
Output:

Menu
1. Add items
2. Display all items
3. Search for items with quantity > 100
4. Update item's unit price and quantity
5. Delete items with quantity 0
6. Quit

Enter your choice: 1

Enter the number of items to add: 3
Enter item number: 1
Enter item name: A
Enter unit price: 99
Enter quantity: 1000

Enter item number: 2
Enter item name: B
Enter unit price: 1000
Enter quantity: 3

Enter item number: 3
Enter item name: C
Enter unit price: 0
Enter quantity: 0

Menu

1. Add items
2. Display all items
3. Search for items with quantity > 100
4. Update item's unit price and quantity
5. Delete items with quantity 0
6. Quit

Enter your choice: 2

Item Number: 1
Item Name: A
Unit Price: 99.0
Quantity: 100

Item Number: 2
Item Name: B
Unit Price: 1000.0
Quantity: 3

Item Number: 3
Item Name: C
Unit Price: 0.0
Quantity: 0

Menu 

1. Add items
2. Display all items
3. Search for items with quantity > 100
4. Update item's unit price and quantity
5. Delete items with quantity 0
6. Quit

Enter your choice: 4

Enter item number to update: 2
Enter new unit price: 10
Enter new quantity: 22

Item updated successfully!

Menu

1. Add items
2. Display all items
3. Search for items with quantity > 100
4. Update item's unit price and quantity
5. Delete items with quantity 0
6. Quit

Enter your choice: 5

Items with quantity 0 deleted successfully!

Menu

1. Add items
2. Display all items
3. Search for items with quantity > 100
4. Update item's unit price and quantity
5. Delete items with quantity 0
6. Quit

Enter your choice: 2

Item Number: 1
Item Name: A
Unit Price: 99.80
Quantity: 100

Item Number: 2
Item Name: B
Unit Price: 10.0
Quantity: 22

Menu
1. Add items
2. Display all items
3. Search for items with quantity > 100
4. Update item's unit price and quantity
5. Delete items with quantity 0
6. Quit

"""
