from nltk import word_tokenize
from gtts import gTTS
from nltk.corpus import stopwords
from playsound import playsound
import speech_recognition as sr
import webbrowser
import os

def gtts_audio(tts):
    x = open(fileP, "wb+")
    tts.write_to_fp(x)
    x.close()
    playsound(fileP)
    os.remove(fileP)
def update_wordkey(raw,words):
    raw_index=-1
    for w in raw:
        raw_index = raw_index +1
        if w in words:
            raw[raw_index] = w.upper()
    print(str(raw))

r = sr.Recognizer()
mic = sr.Microphone()
cont = 0
while True:
    cont = cont + 1
    with mic as source:
        r.adjust_for_ambient_noise(source)
        r.record(source, duration=1)
        print('Por favor habla')
        audio = r.listen(source)
        try:
            transcript = r.recognize_google(audio, language='es-us')
            transcript_raw =str(format(transcript))
            trans_lower =transcript_raw.lower()
            print(trans_lower)
            if trans_lower == 'hola eduardo':
                fileP = 'archivo.mp3'
                tts = gTTS(text='Hola soy tu asistente virtual,¿en que puedo ayudarte?', lang='es-us')
                gtts_audio(tts)
                break
            elif cont <= 2:
                fileP = 'archivo.mp3'
                tts =gTTS(text='no te puedo entender te, por favor llamame como, hola eduardo  ', lang='es-us')
                gtts_audio(tts)
            elif cont> 2 or cont <5:
                cont = 0
        except sr.UnknownValueError:
            print('hijole no funciono')

while True:
    with mic as source:
        r.adjust_for_ambient_noise(source)
        r.record(source, duration=1)
        print('Por favor habla')
        audio = r.listen(source)
        try:
            transcript = r.recognize_google(audio, language='es-us')
            transcript_raw = str(format(transcript))
            trans_lower = transcript_raw.lower()
            print(trans_lower)
            if trans_lower =='apágate' or trans_lower =='apaga te'  :
                tts = gTTS(text='Espera un momento, apagando', lang='es-us')
                gtts_audio(tts)
                break
            tts = gTTS(text='Espera un momento', lang='es-us')
            gtts_audio(tts)
            raw = word_tokenize(trans_lower)
            print(raw)
            words = raw
            wordsFiltered = ''
            stop_w = set(stopwords.words('spanish'))
            for w in words:
                if w not in stop_w:
                    wordsFiltered = wordsFiltered + ' ' +w
            raw_fil = wordsFiltered
            word_key = word_tokenize(raw_fil)
            print(word_key)
            for w in raw:
                if w =="busca"  or w=='búscame':
                    update_wordkey(raw, word_key)
                    if w=="busca":
                        update_wordkey(raw, word_key)
                        x = trans_lower.lstrip('busca')
                    else:
                        update_wordkey(raw, word_key)
                        x = trans_lower.lstrip('búscame')
                    fileP = 'archivo.mp3'
                    tts = gTTS(text='Estos son los resultados'+ x, lang='es-us')
                    gtts_audio(tts)
                    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
                    webbrowser.get(chrome_path).open_new('google.com/search?q=' + x)
                elif w =="dime":
                    update_wordkey(raw, word_key)
                    x = trans_lower.lstrip('dime')
                    print(x)
                    fileP = 'archivo.mp3'
                    tts = gTTS(text='Estos son los resultados' + x, lang='es-us')
                    gtts_audio(tts)
                    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
                    webbrowser.get(chrome_path).open_new('google.com/search?q='+ x)
                elif w =='dame':
                    update_wordkey(raw, word_key)
                    x = trans_lower.lstrip('dame')
                    print(x)
                    fileP = 'archivo.mp3'
                    tts = gTTS(text='Estos son los resultados' + x, lang='es-us')
                    gtts_audio(tts)
                    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
                    webbrowser.get(chrome_path).open_new('google.com/search?q=' + x)
                elif w=='investígame':
                    update_wordkey(raw, word_key)
                    x = trans_lower.lstrip('investigame')
                    print(x)
                    fileP = 'archivo.mp3'
                    tts = gTTS(text='Estos son los resultados' + x, lang='es-us')
                    gtts_audio(tts)
                    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
                    webbrowser.get(chrome_path).open_new('google.com/search?q=' + x)
            fileP = 'archivo.mp3'
            tts = gTTS(text='¿En que más puedo ayudarte?', lang='es-us')
            gtts_audio(tts)
        except sr.UnknownValueError:
            print('lo siento compare')


