t = list()
count = 0

#lectura de la lista
while True :
        value = input("Digite el valor de la lista: ")
        if value != "fin" :
            t.append(value)
            count = count + 1 
        elif value == "fin" :
            break

#primera función
def recortar(t) :
     del t[-1]
     del t[0]
     return None

#segunda función
def medio(t) : 
    return(t)

print(recortar(t))
print(medio(t))

