import nltk
from nltk.book import *
'''
Parte 1
cantidadPalabras =len(text3) # te da la cantidad de palabras
print('Cantidad de palabras ', cantidadPalabras)
vocabulario1 = len(set(text3)) #la cantidad de vocabulario
print('Cantidad de palabras distintas ', vocabulario1)
print('Lista del vocabulario alfa numerico ',  sorted(set(text3)))
text = text3.generate()
tokens = [t for t in text.split()] #bucle para divir todas las palabras
freq = nltk.FreqDist(tokens) #Distribuición de toda los tokens
for key,val in freq.items():#bucle recorre todos los ítems palabra y valor
    print(str(key) + ':' + str(val)) #imprime el llave y el valor del item
'''

'''
Parte 2
text2.dispersion_plot(["Elinor", "Marianne", "Edward", "Willoughby"])
'''

'''
Parte 3
a = sorted([w for w in set(text5) if w.startswith('C') or w.startswith('c')])#startwith es para las letras que comiencen así al principio
print(a)
'''

'''
Parte 4
V = set(text3)
long_words = [w for w in V if len(w) == 4]
print(sorted(long_words))
D = text3
vocab = [w for w in D if len(w) == 4]
fdist1 = FreqDist(vocab)
vocabulary = fdist1.most_common()
print(vocabulary)
'''

'''
parte 5
bookMobyDick = text1 # Cargamos el primer libro (Moby Dick)
numCharacters = sum([len(words)  for words in bookMobyDick ]) # Sumamos la cantidad de caracteres en cada palabra
print('Cantidad de caracteres en Moby Dick:', numCharacters)

numWords =len(bookMobyDick) # Obtenemos la cantidad de "tokens" (palabras y signos de puntuación) del libro
print('Cantidad de palabras en el libro:', numWords)

meanCharactersWord = numCharacters / numWords
print('Promedio de caracteres por palabra:', meanCharactersWord)
'''
