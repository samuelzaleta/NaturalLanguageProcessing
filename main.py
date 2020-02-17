import nltk
from nltk.corpus import PlaintextCorpusReader
from nltk import word_tokenize

corpus_root ='/BUAP/Tareas/EstudioCLaudia/texto'
micorpus = PlaintextCorpusReader(corpus_root, '.*')
tokens =micorpus.words('texto1.txt')

filteredWords = [ # Palabras filtradas es igual a la lista resultante de
    tag_word[0] # La palabra (elemento 0 de la pareja)
    for tag_word in nltk.pos_tag(tokens, tagset='universal') # Por cada una de las palabras etiquetadas en el corpus usando el tagset universal
    if tag_word[1] in ['NOUN', 'VERB'] # solo sí es un verbo o un sustantivo
]
print(filteredWords)
'''
>>> raw = 'I do not like green eggs and ham, I do not like them Sam I am!'
>>> tokens = nltk.word_tokenize(raw)
>>> default_tagger = nltk.DefaultTagger('NN')
>>> default_tagger.tag(tokens)
'''
'''
Parte 2
Pida una dirección de un documento de texto, abralo y muestrelo. Genere un archivo de texto 
en el que se muestren solamente los verbos y los sustantivos del documento de texto.
'''
