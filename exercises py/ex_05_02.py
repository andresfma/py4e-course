xmax = None
xmin = None
while True :
    sval = input("Enter a number: ")
    if sval == "done" :
        break
    try :
        ival = int(sval)
    except :
        print("Invalid input")
        continue
    #max
    if xmax is None or ival > xmax :
        xmax = ival
    #min
    if xmin is None or ival < xmin :
        xmin = ival

#result
print("Maximum is", xmax)
print("Minimum is", xmin)