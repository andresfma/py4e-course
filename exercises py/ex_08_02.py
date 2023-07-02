manejador = open('mbox.txt')

for linea in manejador:
    linea = linea.rstrip()
    palabras = linea.split()
    # print ('Depuración:', palabras)
    if len(palabras) == 0 or palabras[0] != 'From' : 
        continue
    # print(linea)
    print(palabras[2])  

if len(palabras) == 0 or palabras[0] != 'From':
    print("No cumple")