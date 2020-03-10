import nltk
from nltk.corpus import PlaintextCorpusReader
from nltk import word_tokenize
from nltk.corpus import wordnet as wn
'''Parte 1 Abra un documento y muestrelo en pantalla'''

corpus_root ='/BUAP/Tareas/EstudioCLaudia/texto-tarea4'
mi_corpus = PlaintextCorpusReader(corpus_root, '.*')
'''
texto = mi_corpus.raw('crimeandpunishment.txt')
print(texto)
'''


'''
Parte 2 Separelo en oraciones y muestre cada oración numerada 
(1 para la primera oración, 2 para la segunda, etc) 
, pregunte al usuario que numero de oración desea seleccionar'''

oraciones = mi_corpus.sents('crimeandpunishment.txt')

def separar_numerar_oraciones(texto):
    key = 0
    for sent in oraciones:
        key = key + 1
        if sent:
            print(str(key) + ':' + str(sent))
separar_numerar_oraciones(oraciones)
numero = int(input("¿que oración quieres?"+ "\n"))
sent =numero - 1
'''Parte 3
Con la oración seleccionada cambie por sinónimos 
tres sustantivos de la oración (los tres son los que usted elija) y reescriba la oración.
'''
list_oracion = oraciones[sent]
print(list_oracion)
filteredWords = [tagword[0] for tagword in nltk.pos_tag(oraciones[sent], tagset='universal') if tagword[1] in ['NOUN']]
print("los sustantivos de la oracion son:", filteredWords)

sustantivo1 = input("Elige el sustantivo1 que quieres cambiar" + "\n")
cambio1 =  input("Del sustantivo1 por que sinonimos quieren cambiarlo" + "\n")
sustantivo2 = input("Elige el sustantivo2 que quieres cambiar" + "\n")
cambio2 =  input("Del sustantivo2 por que sinonimos quieren cambiarlo" + "\n")
sustantivo3 = input("Elige el sustantivo3 que quieres cambiar" + "\n")
cambio3 =  input("Del sustantivo3 por que sinonimos quieren cambiarlo" + "\n")

def filtaroracio(texto1,sinonimo1,texto2,sinonimo2,texto3,sinonimo3):
    keyword = 0
    list_oracion_sinomino =list_oracion
    for word in list_oracion_sinomino:
        keyword = keyword + 1
        if texto1 == word:
            list_oracion_sinomino[keyword - 1] =sinonimo1
        if texto2 == word:
            list_oracion_sinomino[keyword - 1] = sinonimo2
        if texto3 == word:
            list_oracion_sinomino[keyword - 1] = sinonimo3
    return list_oracion_sinomino

nueva_oracion =filtaroracio(sustantivo1,cambio1,sustantivo2,cambio2,sustantivo3,cambio3)
print(nueva_oracion)
'''
Parte 4
Separe la oración en tokens y permita al usuario elegir uno de los tokens, 
para el token seleccionado imprima sus hipónimos, hiperónimos, merónimos, holónimos, consecutivos lógicos y antónimos.
'''
def tokens(sent, palabra):
    keyword = 0
    new_sent = sent
    for word in new_sent:
        keyword = keyword + 1
        if palabra == word:
            synsent_palabra = wn.synset(palabra + ".n.01")
            lemma_synsent = synsent_palabra.lemmas()
            su_hiponimo = synsent_palabra.hyponyms()
            if su_hiponimo:
                print("Estos son sus hiponimos de ",palabra + ":",sorted(su_hiponimo[0:]))
            else:print("No se encontraron hiponimos")

            su_hiperonimos =synsent_palabra.hypernyms()
            if su_hiperonimos:
                print("Estos son sus hyperonimos",palabra + ":",sorted(su_hiperonimos[0:]))
            else: print("No se encontraro hipernomios")

            su_holonimo = synsent_palabra.member_holonyms()
            if su_holonimo:
                print("Estos son sus holonimos de ",palabra + ":", su_holonimo)
            else: print("Para esa palabra no se encontraron holonimos")
            su_consecutivo_logico = synsent_palabra.entailments()
            if su_consecutivo_logico:
                print("Estos son sus consecutivos logico de ",palabra + ":", su_consecutivo_logico)
            else: print("Para esa plabra no se encontraron consecutivos logicos")
            print(lemma_synsent)
            '''
             lemma_palabra = wn.lemma(palabra + ".n.01")
            su_antonimo =  lemma_palabra.antonyms()
                        if su_antonimo:
                print("Estos son sus antonimos de ",palabra + ":", su_antonimo)
            else: print("Para esa palabra no se encontraron antonimos")
            '''


token = input("Elige la palabra que quieres su hiponimo y hiperonimo" + "\n")

tokens(nueva_oracion,token)