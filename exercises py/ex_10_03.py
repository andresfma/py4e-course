inp = input("Ingrese el nombre del archivo: ")
l = list()
try :
    file = open(inp)
except :
    print("El archivo no se encuentra")
    exit()

import string
d = dict()

for linea in file :
    linea = linea.translate(str.maketrans("","",string.punctuation))
    linea = linea.lower()
    palabras = linea.split()
    for palabra in palabras :
        for letra in palabra :
            if letra not in d :
                d[letra] = 1
            else :
                d[letra] += 1

for k, v in d.items() :
    l.append((v,k))

l.sort(reverse = True)

for k, v in l :
    print(k, v)

#romeo.txt