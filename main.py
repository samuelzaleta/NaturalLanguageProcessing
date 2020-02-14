import nltk



'''
print(nltk.corpus.gutenberg.fileids()) #solicite ver los identificadores de archivo
---
emma = nltk.corpus.gutenberg.words('austen-emma.txt') #Elija el primero de estos textos, Emma de Jane Austen, y asígnele un nombre corto, emma
print(len(emma)) #cuentas plabras tiene
print(emma.concordance("surprize")) #buscar corcindancia de la palabra sorpresa en emma
-----
from nltk.corpus import gutenberg #importar el paquete gutenber y no tener que poner corpus
gutenberg.fileids() #['austen-emma.txt', 'austen-persuasion.txt', 'austen-sense.txt', ...]
emma = gutenberg.words('austen-emma.txt')
print(emma)
-----
**Este programa muestra tres estadísticas para cada texto: longitud promedio de palabras, longitud promedio de oraciones y 
**la cantidad de veces que cada elemento de vocabulario aparece en el texto en promedio 
from nltk.corpus import gutenberg #un programa corto para mostrar otra información sobre cada texto,
for fileid in gutenberg.fileids(): #un bucle sobre todos los valores fileids()
    num_chars = len(gutenberg.raw(fileid)) #raw es para caracteres , La función raw () nos proporciona el contenido del archivo sin ningún procesamiento lingüístico. 
    num_words = len(gutenberg.words(fileid)) #palabras
    num_sents = len(gutenberg.sents(fileid)) # divide el texto en sus oraciones, donde cada oración es una lista de palabras 
    num_vocab = len(set(w.lower() for w in gutenberg.words(fileid))) # .lower devuelve el valor en minusculas o upper() minusculas 
    print(round(num_chars/num_words), round(num_words/num_sents), round(num_words/num_vocab), fileid) #round() para repondaear numeros
----
from nltk.corpus import gutenberg
print(len(gutenberg.raw('blake-poems.txt'))) #nos dice cuántas letras aparecen en el texto, incluidos los espacios entre las palabras.
----
from nltk.corpus import gutenberg
macbeth_sentences = gutenberg.sents('shakespeare-macbeth.txt')
print(macbeth_sentences) # imprime la sentencias 
print(macbeth_sentences[1116]) #te imprime la sentencia del indice 
longest_len = max(len(s) for s in macbeth_sentences)
print([s for s in macbeth_sentences if len(s) == longest_len])  #imprime la sentencia más larga
----
from nltk.corpus import brown
print(brown.categories()) #imprimir categorias
print(brown.words(categories = 'news'))
print(brown.words (fileids = [ 'cg22' ]))
print(brown.sents (categories = [ 'news' , 'editorial' , 'reviews' ]))
----
Comparemos géneros en su uso de verbos modales
from nltk.corpus import brown
news_text = brown.words(categories='news')
fdist = nltk.FreqDist(w.lower() for w in news_text)
modals = ['can', 'could', 'may', 'might', 'must', 'will']
for m in modals:
    print(m + ':', fdist[m], end=' ') #Necesitamos incluir end = '' para que la función de impresión ponga su salida en una sola línea
-----
cfd = nltk.ConditionalFreqDist(
    (genre, word)
        for genre in brown.categories()
        for word in brown.words(categories=genre))
genres = ['news', 'religion', 'hobbies', 'science_fiction', 'romance', 'humor']
modals = ['can', 'could', 'may', 'might', 'must', 'will']
print(cfd.tabulate(conditions=genres, samples=modals)) #tabular
                  can could   may might  must  will 
           news    93    86    66    38    50   389 
       religion    82    59    78    12    54    71 
        hobbies   268    58   131    22    83   264 
science_fiction    16    49     4    12     8    16 
        romance    74   193    11    51    45    43 
          humor    16    30     8     8     9    13 
----
from nltk.corpus import inaugural
cfd = nltk.ConditionalFreqDist(
           (target, fileid[:4])
           for fileid in inaugural.fileids()
           for w in inaugural.words(fileid)
           for target in ['america', 'citizen']
           if w.lower().startswith(target))
cfd.plot()
---
print(nltk.corpus.cess_esp.words ())# Palabras en español
----
**
El último de estos corpus, udhr , contiene la Declaración Universal de Derechos Humanos en más de 300 idiomas. 
Los fileids para este corpus incluyen información sobre la codificación de caracteres utilizada en el archivo, como UTF8 o Latin1 . 
Usemos una distribución de frecuencia condicional para examinar las diferencias en la longitud de las palabras 
para una selección de idiomas incluidos en el corpus udhr.
**
from nltk.corpus import udhr
languages = ['Chickasaw', 'English', 'German_Deutsch',
     'Greenlandic_Inuktikut', 'Hungarian_Magyar', 'Ibibio_Efik']
cfd = nltk.ConditionalFreqDist(
           (lang, len(word))
           for lang in languages
           for word in udhr.words(lang + '-Latin1'))
cfd.plot(cumulative=True)
----
from nltk.corpus import gutenberg
raw = gutenberg.raw( "burgess-busterbrown.txt" )
print(raw[1:20]) #caracteres 
palabras = gutenberg.words( "burgess-busterbrown.txt" )
print(palabras[1:20]) #palabras
sents = gutenberg.sents( "burgess-busterbrown.txt" )
print(sents[1:20]) #sentencias
----
#Cargando tu propio Corpus
**el corpus debe estar en una carpeta solo, en .txt utf8
Ejemplo 1 PlaintextCorpusReader
from nltk.corpus import PlaintextCorpusReader
corpus_root = '/usr/share/dict' [1]
wordlists = PlaintextCorpusReader(corpus_root, '.*') [2]
wordlists.fileids()
Ejemplo 2 BracketParseCorpusReader
corpus_root = r"C:\corpora\penntreebank\parsed\mrg\wsj" [1]
file_pattern = r".*/wsj_.*\.mrg" [2]
ptb = BracketParseCorpusReader(corpus_root, file_pattern)
ptb.fileids()
----
**Condiciones y eventos
Una distribución de frecuencia cuenta eventos observables, como la aparición de palabras en un texto. 
Una distribución de frecuencia condicional necesita emparejar cada evento con una condición. 
Entonces, en lugar de procesar una secuencia de palabras [1], tenemos que procesar una secuencia de pares [2]:
text = [ 'The' , 'Fulton' , 'County' , 'Grand' , 'Jury' , 'said' , ...][1]
pares = [( 'noticias' , 'El' ), ( 'noticias' , 'Fulton' ), ( 'noticias' , 'Condado' ), ...][2]
----
fileids()	the files of the corpus
fileids([categories])	the files of the corpus corresponding to these categories
categories()	the categories of the corpus
categories([fileids])	the categories of the corpus corresponding to these files
raw()	the raw content of the corpus
raw(fileids=[f1,f2,f3])	the raw content of the specified files
raw(categories=[c1,c2])	the raw content of the specified categories
words()	the words of the whole corpus
words(fileids=[f1,f2,f3])	the words of the specified fileids
words(categories=[c1,c2])	the words of the specified categories
sents()	the sentences of the whole corpus
sents(fileids=[f1,f2,f3])	the sentences of the specified fileids
sents(categories=[c1,c2])	the sentences of the specified categories
abspath(fileid)	the location of the given file on disk
encoding(fileid)	the encoding of the file (if known)
open(fileid)	open a stream for reading the given corpus file
root	if the path to the root of locally installed corpus
readme()	the contents of the README file of the corpus
---
---
'''

