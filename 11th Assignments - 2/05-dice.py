import random

while True:
    x=input("Press enter to roll dice! (q to quit) ")

    if x == 'q':
        break

    else:
        print(random.randint(1,6))
