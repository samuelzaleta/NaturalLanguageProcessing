import nltk
from nltk.corpus import PlaintextCorpusReader

corpus_root ='/BUAP/Tareas/EstudioCLaudia/texto'
mi_corpus = PlaintextCorpusReader(corpus_root, '.*')
tokens =mi_corpus.words('texto1.txt')

def filtar_sustantivos_y_verbos(tokens):
    filteredWords = [  # Palabras filtradas es igual a la lista resultante de
        tagword[0]  # La palabra (elemento 0 de la pareja)
        for tagword in nltk.pos_tag(tokens, tagset='universal')
        # Por cada una de las palabras etiquetadas en el corpus usando el tagset universal
        if tagword[1] in ['NOUN', 'VERB'] ] # solo sí es un verbo o un sustantivo
    return filteredWords

verboSustan = str(filtar_sustantivos_y_verbos(tokens))

archivo1= open("archivo1-problema2.txt", "w+", encoding="utf-8")
archivo1.write(verboSustan)
archivo1.close()

#Texto en ingles prueba
tokens1 =mi_corpus.words('crimeandpunishment.txt')

verboSustan1 = str(filtar_sustantivos_y_verbos(tokens1))
archivo2= open("archivo2-problema2.txt", "w+", encoding="utf-8")
archivo2.write(verboSustan1)
archivo2.close()
'''
Parte 2
Pida una dirección de un documento de texto, abralo y muestrelo. Genere un archivo de texto 
en el que se muestren solamente los verbos y los sustantivos del documento de texto.
'''
