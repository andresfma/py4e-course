eng2sp = dict()
text = open("words.txt")
count = 0

#Conversión del texto en palabras individuales contenidos en una lista
for line in text :
    words = line.split()
    for word in words : #Recorrido de cada palabra y adición de key/value al dict creado
        count += 1
        eng2sp.update({word:count})
# print(eng2sp)
print(eng2sp)
print("with" in eng2sp)