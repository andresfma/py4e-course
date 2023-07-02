import socket

url = input("URL-")

try :
    host = url.split("/")[2]
    misock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    misock.connect((host, 80))
    cmd = 'GET "url" HTTP/1.0\r\n\r\n'.encode()
    misock.send(cmd)
    count = b"" #cadena de bytes vacíos
    carac_total = 0
    
    #recorrido y guardado de toda la cadena de bits de la solicitud
    while True:
        datos = misock.recv(512)
        if len(datos) < 1: break
        count += datos
        carac_total = len(datos)
        if carac_total >= 2000 : break

    misock.close()

    contenido = count.decode()
    contenido_short = contenido[:2000]
    print(contenido_short)
    print("El número de carácteres es de:", len(contenido_short))

except :
    print("URL invalida")
    
# http://data.pr4e.org/romeo.txt
# https://en.wikipedia.org/wiki/Boulton_and_Park