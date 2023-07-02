inp = input("Ingresa un nombre de archivo: ")
ndays = dict()

#busqueda de lineas que comienzen por From
try :
    op_file = open(inp)
except :
    print("El archivo no se encuentra")

#Conversión de texto a listas de palabras por lineas
for lines in op_file :
    lines = lines.rstrip()
    words = lines.split()
    if len(words) == 0 or words[0] != "From" : continue #obtención de palabras que comienzan por From
    if words[1] not in ndays : #Indice [2] de la lista que coincide con el día de envío 
        ndays[words[1]] = 1
    else :
        ndays[words[1]] += 1

print(ndays)