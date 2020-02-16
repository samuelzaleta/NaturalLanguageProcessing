import nltk
import urllib.request
import re
from bs4 import BeautifulSoup
from nltk import word_tokenize

def tratamiento_html(text):
    soup = BeautifulSoup(text, "html.parser") #elimina elm etiquetado
    text = soup.get_text()  #obtiene el texto
    raw = re.sub('\[[^]]*\]', '', text) #elimina los corchetes
    return raw
def categoria_gramatica(raw):
    tokens = word_tokenize(raw)
    tagged = nltk.pos_tag(tokens)
    return tagged
url = 'https://es.wikipedia.org/wiki/Procesamiento_de_lenguajes_naturales' #URL de la pagina a obtener
webScrapping = urllib.request.urlopen(url) #obtine la información en bruto de la url
html = webScrapping.read() #le da informaciión en bruto
raw = tratamiento_html(html) #hace el tratamiento de la función
numPalabras = str(len(raw))

vocabularioFrecuencia=[] #lista para agarrar el vocabulario
tokens = [t for t in raw.split()]
freq = nltk.FreqDist(tokens)
for key, val in freq.items():
    vocabularioFrecuencia.append(str(key) + ':' + str(val))

filterList = ", ".join(vocabularioFrecuencia) #filtra la lista
vocabularioFrecuenciaString = str(filterList) #parsea en string

archivo1 = open("archivo1-problema1.txt", "w+",encoding="utf-8")
archivo1.write("Texto completo" + '\n'+ raw  +  '\n' +
              'El vocabulario y su frecuencia'+ '\n' +vocabularioFrecuenciaString +'\n' +
              'El número de palabras que tiene la página. '+'\n' + numPalabras)
archivo1.close()


etiquetadoGramatical = str(categoria_gramatica(raw))
archivo2 = open("archivo2-problema1.txt", "w+", encoding="utf-8")
archivo2.write(etiquetadoGramatical)
archivo2.close()



'''

    

3.	Pida una dirección de la web y genere un archivo de texto que contenga la siguiente información: 
el texto de la página web sin etiquetas HTML, el vocabulario y su frecuencia, el número de palabras que tiene la página. 
Genere un segundo archivo de texto en donde almacene el texto de la página correctamente etiquetado con su categoría gramatical.
'''