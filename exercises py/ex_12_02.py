from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter -")
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

tags = soup("span")
count = 0
sm = 0
for tag in tags :
    # print(tag)
    # print('CLASS:', tag.get('class', None)) devuelve el valor de la etiqueta solicitada
    # print(tag.contents[0])
    # print('Attrs:', tag.attrs) devuelve los atributos de esa etiqueta de html en general
    number = int(tag.contents[0])
    count += 1
    sm = number + sm

print(count, sm)
