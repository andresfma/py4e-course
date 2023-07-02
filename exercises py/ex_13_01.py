import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#Apertura de url y consumo de datos
url = input('URL: ')

print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)

data = uh.read()
print('Retrieved', len(data), 'characters')

#Manejo de XML
tree = ET.fromstring(data)

counts = tree.findall('.//count')
print("Count:", len(counts))
sum_count = 0

for number in counts:
    count_value = int(number.text)
    sum_count += count_value

print("Sum:", sum_count)

# http://py4e-data.dr-chuck.net/comments_1798872.xml