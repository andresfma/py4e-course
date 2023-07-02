def cuenta(cadena, letra) :
    palabra = str(cadena)
    contador = 0
    for x in palabra :
        if x == letra :
            contador = contador + 1
    return contador
    
print(cuenta("banana", "a"))
print(cuenta("aaaaaaaaaa", "a"))
