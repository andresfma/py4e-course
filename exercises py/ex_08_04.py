romeo = open("romeo.txt")
t1 = list()
for i in romeo :
    t = i.split()
    for j in t:
        if j not in t1 :
            t1.append(j)
t1.sort()
print(t1)