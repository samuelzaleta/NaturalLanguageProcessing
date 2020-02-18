from nltk.corpus import wordnet as wn
print(wn.synsets('bank')) # doctest: +ELLIPSIS +NORMALIZE_WHITESPACE
print(wn.synsets('motorcar'))
print(wn.synsets('car'))
print(len(wn.synsets('car')))
print(wn.synset('car.n.01').lemma_names()) #sinonimos con lemman:names; synset muestra uno en siyn en particular
print(wn.synset('car.n.02').lemma_names()) #
print(wn.synset('car.n.01').definition()) #defición
print(wn.synset('car.n.02').definition()) #ejemplo de uso
print(wn.synset('car.n.01').examples())

print('\n')
print(wn.synset('car.n.01').lemmas()) #me da los synset y el sentido
print(wn.lemma('car.n.01.automobile'))

#hyponimios
print('hyponimios')
motorcar = wn.synset('car.n.01')
types_of_motorcar =motorcar.hyponyms()
print(sorted(types_of_motorcar[0:]))

print (sorted(lemma.name()
    for synset in types_of_motorcar
    for lemma in synset.lemmas()))
#hipernomios
print('hipernomios')
motorcar2 = wn.synset('car.n.01')
types_of_motorcar2 =motorcar2.hypernyms()
print(sorted(types_of_motorcar2[0:]))

print (sorted(lemma.name()
    for synset in types_of_motorcar2
    for lemma in synset.lemmas()))

paths = motorcar.hypernym_paths()
print(len(paths))
print([synset.name() for synset in paths[0]])
print([synset.name() for synset in paths[1]])


print('meronimia')
print(wn.synset('car.n.01').part_meronyms()) #muestra las partes de algo

print(wn.synset('tree.n.01').substance_meronyms()) #

print('holonimos')
print(wn.synset('tree.n.01').member_holonyms())
#Verbos
print('verbos')
print(wn.synset('walk.v.01').entailments()) #lo que involucra la accion
print(wn.lemma('supply.n.02.supply').antonyms()) #antonimo sirve para verbos y sustantivos