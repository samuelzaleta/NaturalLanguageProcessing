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

'''la funcion tokens pertenece a la parte 4'''
def tokens(sent,palabra):
    keyword = 0
    sent
    for word in sent:
        keyword = keyword + 1
        if palabra == word:
            synsent_palabra = wn.synset(palabra + ".n.01")
            s_palabra = str(synsent_palabra)
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

            antonimo = [str(lemma.name()) for lemma in synsent_palabra.lemmas()]
            el_antonimo = str(palabra + ".n.01." + antonimo[0])
            su_antonimo = wn.lemma(el_antonimo).antonyms()
            print(antonimo)
            if su_antonimo:
                print("Estos son sus antonimos de ", palabra + ":", su_antonimo)
            else: print("Para esa palabra no se encontraron antonimos")

separar_numerar_oraciones(oraciones)
numero = int(input("¿que oración quieres?"+ "\n"))
sent =numero - 1
list_oracion = oraciones[sent]
print(list_oracion)
'''Parte 3
Con la oración seleccionada cambie por sinónimos 
tres sustantivos de la oración (los tres son los que usted elija) y reescriba la oración.
'''
filteredWords = [tagword[0] for tagword in nltk.pos_tag(oraciones[sent], tagset='universal') if tagword[1] in ['NOUN']]
print("los sustantivos de la oracion son:", filteredWords)
cont_sustantivos = 0
keyword = 0
for sustantivo in filteredWords:
    cont_sustantivos = cont_sustantivos + 1
if cont_sustantivos ==1:
    sustantivo1 = filteredWords[0]
    cambio1 = input("Del " + sustantivo1 + " por que sinonimos quieres cambiarlo" + "\n")
    list_oracion_sinomino = list_oracion
    for word in list_oracion_sinomino:
        keyword = keyword + 1
        if sustantivo1 == word:
            list_oracion_sinomino[keyword - 1] = cambio1
            print(list_oracion_sinomino)
            '''Parte 4'''
            token = input("Elige la palabra(sustantivo o verbo) que quieres su hiponimo, hiperonimo, meronion, holominio, ect " + "\n")
            filWords = [tagword[0] for tagword in nltk.pos_tag(list_oracion_sinomino, tagset='universal') if
                             tagword[1] in ['NOUN', 'VERB']]
            for word in filWords:
                if word ==token:
                    tokens(list_oracion_sinomino, token)
                else:
                    print("No se encontraron resultados")

elif cont_sustantivos ==2:
    sustantivo1 = input("Elige el sustantivo1 que quieres cambiar" + "\n")
    cambio1 = input("De " +  sustantivo1 + " por que sinonimo quieres cambiarlo" + "\n")
    sustantivo2 = input("Elige el sustantivo2 que quieres cambiar" + "\n")
    cambio2 =  input("De " + sustantivo2 + " por que sinonimo quieres cambiarlo" + "\n")
    list_oracion_sinomino = list_oracion
    for word in list_oracion_sinomino:
        keyword = keyword + 1
        if sustantivo1 == word:
            list_oracion_sinomino[keyword - 1] = cambio1
        if sustantivo2 == word:
            list_oracion_sinomino[keyword - 1] = cambio2
            print(list_oracion_sinomino)
            '''Parte 4'''
            token = input("Elige la palabra(sustantivo o verbo) que quieres su hiponimo, hiperonimo, meronion, holominio, ect " + "\n")
            filWords = [tagword[0] for tagword in nltk.pos_tag(list_oracion_sinomino, tagset='universal') if
                        tagword[1] in ['NOUN', 'VERB']]
            for word in filWords:
                if word == token:
                    tokens(list_oracion_sinomino, token)
                else:
                    print("No se encontraron resultados")
else:
    sustantivo1 = input("Elige el sustantivo1 que quieres cambiar" + "\n")
    cambio1 = input("De " + sustantivo1 + " por que sinonimo quieres cambiarlo" + "\n")
    sustantivo2 = input("Elige el sustantivo2 que quieres cambiar" + "\n")
    cambio2 = input("De " + sustantivo2 + " por que sinonimo quieres cambiarlo" + "\n")
    sustantivo3 = input("Elige el sustantivo3 que quieres cambiar" + "\n")
    cambio3 = input("De "+ sustantivo3 + " por que sinonimos quieren cambiarlo" + "\n")
    list_oracion_sinomino = list_oracion
    for word in list_oracion_sinomino:
        keyword = keyword + 1
        if sustantivo1 == word:
            list_oracion_sinomino[keyword - 1] = cambio1
        if sustantivo2 == word:
            list_oracion_sinomino[keyword - 1] = cambio2
        if sustantivo3 == word:
            list_oracion_sinomino[keyword - 1] = cambio3
            print(list_oracion_sinomino)
            '''Parte 4'''
            token = input("Elige la palabra(sustantivo o verbo) que quieres su hiponimo, hiperonimo, meronion, holominio, ect " + "\n")
            filWords = [tagword[0] for tagword in nltk.pos_tag(list_oracion_sinomino, tagset='universal') if
                        tagword[1] in ['NOUN', 'VERB']]
            for word in filWords:
                if word == token:
                    tokens(list_oracion_sinomino, token)
                else:
                    print("No se encontraron resultados")

'''
Parte 5.Por último, simule un término de búsqueda y su expansión con sugerencias, es decir, pida un termino y complete utilizando 
las relaciones de Wordnet, por ejemplo, si se teclea "motorcar" se puede sugerir buscar también "car" o "vehicle" o terminos relacionados 
como "motor vehicle", etc.  De al menos tres tipos de sugerencias diferentes para la palabra.
'''
palabraswordnet = input("Que palabra quieres buscar en ingles")
palabrarelacionada = [str(lemma.name()) for lemma in wn.synset(palabraswordnet  + ".n.01").lemmas()]
print(palabrarelacionada)