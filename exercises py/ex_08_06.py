t = list()

while True :
    inp = input("Enter a number: ")
    if inp == "end" : break
    ft = float(inp)
    t.append(ft)
    
xmax = max(t)
xmin = min(t)

print("Máximo: ", xmax)
print("Mínimo: ", xmin)
