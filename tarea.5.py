import string
import nltk
import math
from nltk.corpus import PlaintextCorpusReader
from nltk.tokenize import word_tokenize

'''
Preprocesar cada documento, es decir, eliminar las palabras vacias, utiliza la lista de time.stp.
'''

corpus_root = 'C:\BUAP\Tareas\EstudioClaudia\doñaclau'
reader = PlaintextCorpusReader(corpus_root, '.*')

text = reader.raw('TIME.ALL')  # Texto
documents = text.split('*')
empty_words = reader.raw('TIME.STP')  # Palabras vacias
empty_words_tokens = word_tokenize(empty_words)

array_document = []
for document in documents:
    document_tokens = []
    tokens = word_tokenize(document)

    for token in tokens:
        if token not in empty_words_tokens and token not in string.punctuation:
            document_tokens.append(token)
    array_document.append(document_tokens)

del array_document[0]
del array_document[-1]
result_file_tf = open("corpus-stopword.txt", "w+", encoding="utf-8")
result_file_tf.write(str(array_document))
result_file_tf.close()

'''
Obtener el vocabulario de cada documento almacenando la frecuencia de cada término en dicho documento, 
es decir, el TF. Imprimir la lista de terminos con su frecuencia, por ejemplo, D1 termino TF
'''

TF = []
for document_tokenized in array_document:
    tf = dict()
    freq = nltk.FreqDist(document_tokenized)
    vd = len(document_tokenized)

    for token, count in freq.items():
        result = count / vd

        tf[token] = result
    TF.append(tf)

result_file_tf = open("corpus-tf.txt", "w+", encoding="utf-8")
result_file_tf.write(str(TF))
result_file_tf.close()

'''
Unir el vocabulario de todos los documentos y calcular la frecuencia de los documentos (DF), 
es decir, en cuantos documentos aparece cada término. Imprimir una lista , por ejemplo, Termino, DF
'''

word_freq = dict()
for document_tokenized in array_document:
    uniq_tokens = dict()

    for token in document_tokenized:
        uniq_tokens[token] = 0

    for uniq_token in uniq_tokens:
        if uniq_token not in word_freq:
            word_freq[uniq_token] = 0
        word_freq[uniq_token] += 1

result_file_df = open("corpus-df.txt", "w+", encoding="utf-8")
result_file_df.write(str(word_freq))
result_file_df.close()

'''
Construye los vectores de cada documento utilizando el pesado TF-IDF
'''
idf = dict()

for token, count in word_freq.items():
    if count > 1:
        idf[token] = math.log(len(array_document), count)
    else:
        idf[token] = 0

IDF_TF = []
for tf in TF:
    idf_tf = dict()

    for word, count1 in tf.items():
        count2 = idf[word]
        idf_tf[word] = count1 * count2

    IDF_TF.append(idf_tf)

result_file_idf = open("corpus-idf.txt", "w+", encoding="utf-8")
result_file_idf.write(str(idf))
result_file_idf.close()

result_file_idf_tf = open("corpus-idf-tf.txt", "w+", encoding="utf-8")
result_file_idf_tf.write(str(IDF_TF))
result_file_idf_tf.close()

'''
Construye los los vectores de las 10 primeras consultas utilizando un pesado binario.
'''
vocabulary = dict()  # El vocabulario resultante

queries = []
for document_tokenized in array_document[:10]:
    binary_w = dict()

    for token in document_tokenized:
        if token not in string.punctuation:
            vocabulary[token] = 0
            binary_w[token] = 1

    queries.append(binary_w)

for i in range(len(queries)):
    query = queries[i]
    queries[i] = {**vocabulary, **query}

result_file_binary = open("corpus-binary.txt", "w+", encoding="utf-8")
result_file_binary.write(str(queries))
result_file_binary.close()

'''
Reliza la recuperación de información de estas 10 consultas utilizando la similitud coseno. 
Imprime los documentos que tengan similitud distinta a cero y ordenalos de forma descendente.
'''
Coseno = []
for i in range(len(queries)):
    for j in range(i + 1, len(queries)):
        document1 = queries[i]
        document2 = queries[j]
        sum_mul = 0
        sum_doc1 = 0
        sum_doc2 = 0

        for token, value1 in document1.items():
            value2 = document2[token]

            sum_mul += value1 * value2
            sum_doc1 += value1
            sum_doc2 += value2
        sim = sum_mul / math.sqrt(sum_doc1 * sum_doc2)
        print(sim)
        Coseno.append(sim)
Coseno.sort(reverse=True)
print(Coseno)
