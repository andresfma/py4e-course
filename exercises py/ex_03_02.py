#valores de entrada
horasstr = input("Introduzca las horas: ")

#condicional
try :
    horas = float(horasstr)
except :
    horas = -1
if horas > 0 :
    tarifastr = input("Introduzca la tarifa: ")
    try :
        tarifa = float(tarifastr)
    except :
        tarifa = -1
    if tarifa > 0 :
        if horas <= 40 :
            salbruto = horas*tarifa
        else :
            salbruto = (40*tarifa)+((horas-40)*tarifa*1.5)
        print("Pay:", salbruto)
    else :
        print("Error, por favor introduzca un número")
else :
    print("Error, por favor introduzca un número")