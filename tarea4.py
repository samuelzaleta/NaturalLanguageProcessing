import nltk
import urllib.request
import bs4 as bs
import re
from nltk import word_tokenize

'''
Parte 1
'''
def tratamiento_html(url):
    scraped_data = urllib.request.urlopen(url)
    article = scraped_data.read()
    parsed_article=bs.BeautifulSoup(article,'lxml')
    paragraphs = parsed_article.find_all('p')
    return paragraphs
url = 'https://es.wikipedia.org/wiki/Procesamiento_de_lenguajes_naturales'
paragraphs = tratamiento_html(url)

def separar_numerar_oraciones(parrafo):
    key = 0
    for sent in parrafo:
        key = key + 1
        if key == 1 or key ==2:
            return sent
def archivo(parrafos,resumen):
    archivo1 = open("textooriginal.txt", "w+", encoding="utf-8")
    archivo1.write(parrafos)
    print(archivo1.read())
    archivo1.close()
    archivo2 = open("resumen1.txt", "w+", encoding="utf-8")
    archivo2.write(resumen)
    print(archivo2.read())
    archivo2.close()

def strip_tags(value):
    raw = re.sub(r'<[^>]*?>', '', value)
    return raw
resumen = ''
for p in paragraphs:
    raw = str(p)
    parrafos = strip_tags(raw)
    oraciones  = nltk.sent_tokenize(parrafos)
    resumen = resumen + separar_numerar_oraciones(oraciones)

texto_original  = strip_tags(str(paragraphs))
archivo(texto_original,resumen)
print(texto_original + '\n')
print(resumen)
'''
Parte 2
'''
palabraclave1 = input("Cual es la primera palabra clave del texto" + "\n")
palabraclave2 = input("Cual es la segunda palabra clave del texto" + "\n")
palabraclave3 = input("Cual es la tercera palabra clave del texto" + "\n")
palabraclave4 = input("Cual es la cuarta palabra clave del texto" + "\n")
palabraclave5 = input("Cual es la quienta palabra clave del texto" + "\n")

parraf = 0
orac =0
word = 0
for p in paragraphs:
    raw = str(p)
    parrafo = strip_tags(raw)
    oraciones = nltk.sent_tokenize(parrafo)
    for sent in oraciones:
        for word in sent:
            if word == palabraclave1 or word == palabraclave2 or word == palabraclave2 or word == palabraclave3 or word == palabraclave4 or word == palabraclave5:
                resumen2 = resumen2 + sent

archivo1 = open("resuemn2.txt", "w+", encoding="utf-8")
archivo1.write(resumen2)
print(archivo1.read())
archivo1.close()
