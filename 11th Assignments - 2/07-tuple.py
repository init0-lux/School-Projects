tup = eval(input("Enter the tuple: "))

def frequency(t):
    l=[]
    
    for i in t:
        l.append(i)

    l.sort()

    freq = {}

    for i in l:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1

    for i in freq:
        print(i, "-", freq[i], "times")

frequency(tup)
