list = eval(input("Enter list: "))

def shift(l):
    l.insert(0,l.pop())
    print(l)

shift(list)
