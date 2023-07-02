str = 'X-DSPAM-Confidence:0.8475'
#search :
caracter1 = str.find(":")
#string extraction
address = float(str[caracter1+1:])
print(address)



