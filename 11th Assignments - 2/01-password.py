import csv

def add():
    number = int(input("Enter the number of users to add: "))
    print()
    data = []
    
    for i in range(number):
        userid = input("Enter the userid for user #"+str(i+1)+": ")
        passwd = input("Enter the passwd for user #"+str(i+1)+": ")
        print()
        
        data.append([userid,passwd])
    
    with open("password.csv", 'a') as csvfile:
        csvf = csv.writer(csvfile)
        csvf.writerows(data)

def display():

    print("Users#\t\tPasswords#\n--------------------------")
    with open("password.csv", 'r') as csvfile:
        csvf = csv.reader(csvfile)

        for row in csvf:
            print('\t\t'.join(row))

def search():
    data = {}
    with open("password.csv", 'r') as csvfile:
        csvf = csv.reader(csvfile)
        
        for i in csvf:
            data[i[0]] = i[1]

    while True:
        userid = input("Enter the user id to search for ['n' to quit]: ")

        if userid == 'n':
            break
        if userid in data:
            print("Password =", data[userid])
        else:
            print("Error! User not found!")

add()
print()

display()
print()

search()
