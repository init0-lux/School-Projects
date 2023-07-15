global list

def Push():
    name = input("\nEnter name to push: ")
    list.append(name)
    print()
    Menu()

def Pop():
    print(list.pop(), "popped!\n")
    Menu()

def Display():
    print("\nList Items: ")

    for i in list:
        print(i)
    
    print()
    Menu()

def Menu():
    print("Stack Implementation\n\n")
    print("1. Push\n2. Pop\n3. Display\n4. Quit")

    ch = int(input("\n\nEnter your choice: "))

    if ch == 1:
        Push()
    elif ch == 2:
        Pop()
    elif ch == 3:
        Display()
    else:
        print("\n\nSorry to see you go!")

list = eval(input("Enter list of names (in list format): "))
print()
Menu()
