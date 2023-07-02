inpfile = input("Ingresa el nombre del archivo: ")
inpex = input("Ingresa una expresión regular: ")

try :
    op = open(inpfile)
except :
    print("El archivo no se encuentra")
    exit()

import re
count = 0
for lines in op :
    lines = lines.rstrip()
    x = re.findall(inpex, lines)
    if len(x) > 0 : 
        count += 1

print(inpfile, "tiene", count, "líneas que coinciden con", inpex)

#mbox-short.txt
#^Author

