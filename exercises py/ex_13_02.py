import urllib.request, urllib.parse, urllib.error
import json
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

#Manejo JSON
js = json.loads(data)
info = js["comments"]
sum_number = 0
count = 0

for x in info :
    number = int(x['count'])
    sum_number += number
    count += 1

print("Count:", count)
print("Sum:", sum_number)

# http://py4e-data.dr-chuck.net/comments_1798873.json