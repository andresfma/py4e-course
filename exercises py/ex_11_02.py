inp = input("Ingresa el nombre del archivo: ")
import re

try :
    op = open(inp)
except :
    print("El archivo no se encuentra")
    exit()

suma = 0
count = 0

for lines in op :
    lines = lines.rstrip()
    x = re.findall('^New Revision: ([0-9]+)', lines)
    if len(x) > 0 :
        count += 1
        number = int(x[0])
        suma += number
        prom = suma/count 
        
print(prom)

#mboxlarge.txt
