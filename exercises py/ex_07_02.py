file = input("Nombre del archivo: ")
count = 0
total = 0
try :
    manejador_archivo = open(file)
except :
    if file == "na na boo boo" :
        print("NA NA BOO BOO para ti - Te he atrapado!")
    else :
        print("El archivo '", file, "' no pudo encontrarse")
    exit()
for line in manejador_archivo :
    #identificando todas las líneas de interés
    line = line.rstrip() #sin saltos dobles de interlineado
    if line.find("X-DSPAM-Confidence:") == -1 : continue
     #extraer el dígito decimal
    positionpunt = line.find(":")
    number = float(line[positionpunt+2:])
     #contadores para el promedio
    count = count + 1
    total = total + number
    average = total/count
print("Average spam confidence:", average)




