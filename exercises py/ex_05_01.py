total = 0
count = 0
prom = 0
numbers = []
while True :
    inp = input(">")
    try :
        number = int(inp)
        numbers.append(number)
    except :
        if inp == "end" :
            for x in numbers :
                total = total + x
                count = count + 1
                prom = total/count
            break
        else :
            print("Invalid data")
            continue
print(total, count, prom)


