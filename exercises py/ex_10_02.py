inp = input("Ingresa el nombre del archivo: ")
d = dict()

try :
    fileop = open(inp)
except :
    print("El archivo", inp, "no se encuentra:")
    exit()

#Leer el archivo y crear lineas buscando solo los que comienzan con From
for lines in fileop :
    lines = lines.rstrip()
    lines = lines.split()

    if len(lines) < 1 or lines[0] != "From": continue

    #Uso del diccionario para contar los correos y el número de estos
    hours = lines[5]
    hour = hours.split(":")
    del hour[1:]
    strhour = "".join(hour)
    # print(strhour)
    # print(type(strhour))

    if strhour not in d :
        d[strhour] = 1
    else :
        d[strhour] += 1
    
#Creación de lista de tuplas
lst = list()

for k, v in list(d.items()) :
    lst.append((k,v))

lst.sort() 

for k, v in lst :
    print(k, v)
#mbox-short.txt