#valores de entrada
horasstr = input("Introduzca las horas: ")
tarifastr = input("Introduzca la tarifa: ")

#conversión a int
horas = float(horasstr)
tarifa = float (tarifastr)

#condicional
if horas <= 40 :
    salbruto = horas*tarifa
else :
    salbruto = (40*tarifa)+((horas-40)*tarifa*1.5)

#resultado
print("Pay:", salbruto)