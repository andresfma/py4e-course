#variables 
numberstr = input("Introduzca número (0.0 - 1.0): ")

try :
    number = float(numberstr)
except :
    number = -1
if 0 <= number < 0.6 :
    print("F")
elif number < 0 or number > 1 :
    print("Incorrect punctuation")
elif number >= 0.9 :
    print("A")
elif number >= 0.8 :
    print("B")
elif number >= 0.7 :
    print("C")
elif number >= 0.6 :
    print("D")
