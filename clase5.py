import speech_recognition as sr
'''
r =sr.Recognizer()
print("Entró")
song =sr.AudioFile('OSR_us_000_0010_8k.wav')
with song as source:
 audio =r.record(source)
type(audio)
try:
 text = r.recognize_google(audio)
 print('audio dice:'.format(text))
except:
 print('no se escucha')
'''
'''
Microfono
'''
r = sr.Recognizer()

mic =sr.Microphone()
with mic as source:
 r.adjust_for_ambient_noise(source)
 audio = r.listen(source)
 transcript =r.recognize_google(audio)
 print(transcript)
