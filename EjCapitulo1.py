import nltk
from nltk.book import *
'''
text1.concordance("monstrous")  --Una vista de concordancia nos muestra cada aparición de una palabra dada, junto con algún contexto.
text2.similar("monstrous") ---Ejemplos o palabras similares
text2.common_contexts --(["monstrous", "very"]) nos permite examinar solo los contextos que comparten dos o más palabras, como monstruoso y muy
text4.dispersion_plot (["citizens", "democracy", "freedom", "duties", "America"]) --  la ubicación de una palabra en el texto:
cuántas palabras desde el principio aparece. Esta información posicional se puede mostrar utilizando un diagrama de dispersión .
Cada franja representa una instancia de una palabra, y cada fila representa todo el texto.
text3.generate () -- genera el texto
-----------
imprim =  len(text3)
print(nim)           -- longitud de un texto de principio a fin
-----------
imprim = sorted(text3) ordena el texto de manera alfanumerica
imprim = sorted(set(text3)) --obtenemos una lista ordenada de elementos de vocabulario sin repetir palabras
imprim = len(set(text3)) -- cantidad palabras distintas, puro ser te da la lista
imprim = len (set (text3)) / len (text3) --  medida de la riqueza léxica del texto. El ejemplo siguiente nos muestra que
el número de palabras distintas, está a 6% del número total de palabras, o equivalentemente que cada palabra se usa 16 veces en promedio
imprim = text3.count("smote") -- contar con qué frecuencia aparece una palabra en un texto
100 * text4.count ( 'a' ) / len (text4) -- calcular qué porcentaje del texto está ocupado por una palabra
-------------------
//Definir un metodo //
def  lexical_diversity (text):
     return len(text) / len(set(text))
def  porcentaje (count, total):
     return 100 * count / total
lexical_diversity (text3)
 0.06230453042623537
lexical_diversity (text5)
 0.13477005109975562
percentage(4, 5)
80.0
percentage(text4.count('a'), len(text4))
 1.4643016433938312
--------------------
// definir lista palabras y contar longitud
sent1 = ['Call', 'me', 'Ishmael', '.']
nim = len(sent1)
print(nim)
--------------------
// metodo para diversidad lexica//
def diversidad_lexica(text):
    print(len(text) / len(set(text)))
sent1 = ['Call', 'me', 'Ishmael', '.']
diversidad_lexica(sent1)
diversidad_lexica(text3) //del texto3
--------------------------
argregar un anexo a la lista
sent1 = ['Call', 'me', 'Ishmael', '.']
sent1.append("some")
print(sent1)
---------------
#jugar con los indices
print(len(set(text1)), #cuantas palabras tiene sin repetir sin el set en términos de las palabras y los signos de puntuación que aparecen
      text1.count('sky'), # cuenta cuantas veces aparece
      text4[173], #trae la palabra o signo del indice
      text4.index('awaken'), # te dice que indice es la palabra
      text5[16715: 16735], # imrpimer las palabras de del rango establecido
      text6[1600: 1625]
      )
sent = ['word1', 'word2', 'word3', 'word4', 'word5','word6', 'word7', 'word8', 'word9', 'word10']
print(
    sent[0],
    sent[9],
    sent[5:8],
    sent[:3], # desde el inicio hasta el indice indicado 0-3
    sent[3:] # despues del indice hasta el final 4 - lim
)
# depurar una lista
my_sent = [ 'Valientemente' , 'negrita' , 'Señor' , 'Robin' , ',' , 'cabalgó' , 'adelante' , 'de' , 'Camelot' , '.' ]
noun_phrase = my_sent [1: 4]
print(noun_phrase) #['negrita', 'Señor', 'Robin']
wOrDs = sorted(noun_phrase)
print(wOrDs) #['Robin', 'Señor', 'negrita']
----------------
palabras =len(text1) #cuenta las palabras y signos
print(palabras)
vocab = set(text1) #imprime las palabras no repetidas
print(vocab)
vocab_size =  len(vocab) #las vuelve a leer pero esi igual que in len(set()) donde te dice cuantas palabras son sin repetirse
print(vocab_size)

JUGAR CON CADENAS [Strings]
--------------------------
nombre = 'Monty'
nombre [0]
'M'
nombre [:4]
'Mont'
nombre * 2
 'MontyMonty'
nombre + '!'
Monty!
-------
Separar
a = "this is a string"
a = a.split()# a is converted to a list of strings.
print(a) #['this', 'is', 'a', 'string']
Juntar
sent1 = ['Robin', 'Señor', 'negrita']
a=''.join(sent1) #RobinSeñornegrita
print(a)
-------------------
SIMPLE STATISTICS
------------------
fdist1 = FreqDist(text1) #Distribuición de frencuencia
print(fdist1)
------------------
fdist1 = FreqDist(text1) #odemos inspeccionar el número total de palabras ("resultados") que se han contado
vocabulary1 =fdist1.keys() #nos dan una lista de todos los tipos distintos en el texto
vocabulary2 = fdist1.most_common(50) #La expresión most_common (50) nos da una lista de los 50 tipos más frecuentes en el texto
vocabulary3 = fdist1['whale'] #te trae el indice de la frecuencia de la palabra
print(vocabulary1)
print(vocabulary2)
print(vocabulary3)
-----------------
fdist1 = FreqDist(text1)
fdist1.plot(100, cumulative=True) #Podemos generar una gráfica de frecuencia acumulativa para estas palabras
# lista de palabras con 15 letras alfanumericamente
V = set(text1) #todas la palabras que no se repiten
long_words = [w for w in V if len(w) > 15] #recorra todas las palabras que no tenga 15 caracteres
n =sorted(long_words)  #ordenalas
print(n)
'''

