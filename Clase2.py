import nltk
from nltk.corpus  import PlaintextCorpusReader
corpus_root ='/Users/samue/OneDrive/Documentos/unity/Noticias'
micorpus = PlaintextCorpusReader(corpus_root, '.*')
print(micorpus.fileids())
print(micorpus.words(('noticia1.txt')))
print(nltk.help.upenn_tagset())

'''
import nltk
from nltk.corpus import brown
print(brown.categories()) #trae las categorias
print(brown.words(categories = 'science_fiction')) #trae las palabras
print(brown.fileids(categories ='science_fiction'))

print(brown.words(fileids= ['cm01']))
print(brown.sents(categories = ['news','editorial','reviews']))

print(brown.sents(categories=['news']))
news_text  =brown.words(categories ='news')
fdist = nltk.FreqDist(w.lower() for w in news_text)
modals = ['can' , 'could', 'may', 'might','must','will']
print('news')
for m in modals:
    print(m + ':', fdist[m], end=' ')

news_text  =brown.words(categories ='romance')
fdist = nltk.FreqDist(w.lower() for w in news_text)
modals = ['can' , 'could', 'may', 'might','must','will']
print('romance')
for m in modals:
    print(m + ':', fdist[m], end=' ')


news_text  =brown.words(categories ='science_fiction')
fdist = nltk.FreqDist(w.lower() for w in news_text)
modals = ['can' , 'could', 'may', 'might','must','will']
print('science_fiction')
for m in modals:
    print(m + ':', fdist[m], end=' ')

print(nltk.corpus.cess_esp.words())
'''
'''
from bs4 import BeautifulSoup
import urllib.request
import nltk
from nltk.corpus import stopwords

response = urllib.request.urlopen('https://medlineplus.gov/spanish/schizophrenia.html')
html = response.read()
print(html)
soup = BeautifulSoup(html,"html5lib")
text = soup.get_text(strip=True)
print(text)

tokens = [t for t in text.split()]
freq = nltk.FreqDist(tokens)
for key, val in freq.items():
    print(str(key) + ':' + str(val))

sr = stopwords.words('spanish')
print(sr)

tagged = nltk.pos_tag(tokens)
print(tagged)
'''