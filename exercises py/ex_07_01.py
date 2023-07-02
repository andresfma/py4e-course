file = input("Nombre del archivo: ")

try :
    manejador_archivo = open(file)
except :
    print("El archivo '", file, "' no pudo encontrarse")
    exit()
for line in manejador_archivo :
        line = line.rstrip()
        print(line.upper())






