nm_file = input("Ingrese el nombre del archivo completo: ")
op_file = open(nm_file)
count = 0
for lines in op_file :
    words = lines.split()
    if len(words) == 0 or words[0] != "From": continue
    count = count + 1
    print(words[1])

print("There were", count, "lines in the file with From as the first word")
