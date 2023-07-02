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

    #selección de solo el dominio del correo
    arroba = words[1].find("@")
    direccion = words[1][arroba + 1:]

    #adición del dominio del correo al dict
    if direccion not in ndays : 
        ndays[direccion] = 1
    else :
        ndays[direccion] += 1

print(ndays)