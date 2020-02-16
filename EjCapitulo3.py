'''
**Crimen y castigo obtener en web, no en corpus
**nota agarra tambien las etiquera, excepto en este ejemplo, enlace para intentar
from urllib import request
url = "http://www.gutenberg.org/files/2554/2554-0.txt"
#url = "https://en.wikipedia.org/wiki/Argon2"
response = request.urlopen(url)
raw = response.read().decode('utf8')
print(type(raw))
print(len(raw))
print(raw[:75])
print(raw[75:150])
#print(raw[0:])
--------------------
'''