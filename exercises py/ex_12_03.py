from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter -")
count = input("Enter count:")
position = input("Enter position:")

#contadores
ciclos = int(count)

#numero de veces a realizar el ciclo
while ciclos > 0 :
    ciclos -= 1
    linea = 0
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")

    tags = soup('a')

    for tag in tags:
        linea += 1
        if linea == int(position) :
            url = tag.get('href', None)
            print(tag)
            break
        