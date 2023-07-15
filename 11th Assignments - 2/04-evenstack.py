def Push(lst,stck):
    for i in lst:
        if i%2 == 0:
            stck.append(i)

def POP(l):
    if len(l) > 0:
        print(l.pop(), " Popped!\n")
    else:
        print("List already empty!\n")

def display(st):
    print("Stack Items: ")
    for i in st:
        print(i)

    print()


list = eval(input("Enter the list: "))
print()

stack = []

Push(list,stack)
display(stack)
POP(stack)
display(stack)
