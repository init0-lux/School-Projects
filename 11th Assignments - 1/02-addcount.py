#! /usr/bin/python3

def Add(n):
    with open('jvm.dat', 'a') as f:
        for i in range(n):
            line = input("Enter line " + str(i+1) + ": " )
            f.write(line + "\n")

def words():
    c=0
    with open("jvm.dat", 'r') as f:
        for lines in f:
            line = lines.strip()
            words = line.split()

            for word in words:
                if len(word) > 4:
                    c += 1

    print("Number of words with length >4: ",  c)



n = int(input("Enter number of lines: "));
Add(n)
words()

# Output:
# Enter number of lines: 3
# Enter line 1: aaaaa
# Enter line 2: ff
# Enter line 3: ff
# Number of words with length >4:  1
