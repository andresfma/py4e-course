import socket

url = input("URL-")

try :
    host = url.split("/")[2]
    print(url, host)
    misock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    misock.connect((host, 80))
    cmd = 'GET url HTTP/1.0\r\n\r\n'.encode()
    misock.send(cmd)

    while True:
        datos = misock.recv(512)
        if len(datos) < 1:
            break
        print(datos.decode(),end='')

    misock.close()
except :
    print("URL invalida")
# http://data.pr4e.org/romeo.txt