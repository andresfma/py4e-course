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
    email = lines[1]
    if email not in d :
        d[email] = 1
    else :
        d[email] += 1
    
#Creación de lista de tuplas
lst = list()

for k, v in list(d.items()) :
    lst.append((v,k))

lst.sort(reverse = True) 

for k, v in lst[:1] :
    print(k, v)
#mbox-short.txt