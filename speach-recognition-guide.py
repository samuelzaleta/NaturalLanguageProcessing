import speech_recognition as sr
r =sr.Recognizer() #reconocer el habla
'''
Cada Recognizerinstancia tiene siete métodos para reconocer la voz de una fuente de audio utilizando varias API. Estos son:

recognize_bing(): Discurso de Microsoft Bing
recognize_google(): API de Google Web Speech
recognize_google_cloud(): Google Cloud Speech : requiere la instalación del paquete google-cloud-speech
recognize_houndify(): Houndify por SoundHound
recognize_ibm(): Discurso a texto de IBM
recognize_sphinx(): CMU Sphinx - requiere la instalación de PocketSphinx
recognize_wit(): Wit.ai
De los siete, solo recognize_sphinx()funciona sin conexión con el motor CMU Sphinx.
Los otros seis requieren una conexión a internet.

Los siete recognize_*()métodos de la Recognizerclase requieren un audio_dataargumento.
En cada caso, audio_datadebe ser una instancia de la AudioDataclase SpeechRecognition .
'''

'''
Tipos de archivo admitidos
Actualmente, SpeechRecognition admite los siguientes formatos de archivo:

WAV: debe estar en formato PCM / LPCM
AIFF
AIFF-C
FLAC: debe ser formato FLAC nativo; OGG-FLAC no es compatible
'''
audio = sr.AudioFile('OSR_us_000_0010_8k.wav')
with audio as source:
    sonido = r.record(source)#audio = r.record(source, duration=4)
'''
El record()método, cuando se usa dentro de un withbloque, siempre avanza en la secuencia del archivo.
 Esto significa que si graba una vez durante cuatro segundos y luego vuelve a grabar durante cuatro segundos, 
 la segunda vez devuelve los cuatro segundos de audio después de los primeros cuatro segundos.
...     sonido1 = r.record(source, duration=4)
...     sonido2 = r.record(source, duration=4)
Además de especificar una duración de grabación, el record()método puede recibir un punto de partida específico utilizando el offsetargumento de la palabra clave
sonido = r.record(source, offset=4, duration=3)
'''
'''
Ahora puede invocar recognize_google()para intentar reconocer cualquier discurso en el audio. 
Dependiendo de la velocidad de su conexión a Internet, 
es posible que tenga que esperar varios segundos antes de ver el resultado.
'''
#print(r.recognize_google(sonido))
'''
La Microphoneclase
Abra otra sesión de intérprete y cree una instancia de la clase reconocedora.
'''
mic = sr.Microphone()
'''
Al igual que la AudioFileclase, Microphonees un administrador de contexto. 
Puede capturar la entrada del micrófono utilizando el listen()método de la Recognizerclase dentro del withbloque. 
Este método toma una fuente de audio como primer argumento y registra la entrada de la fuente hasta que se detecte el silencio.
'''
with mic as source1:
    r.adjust_for_ambient_noise(source1)
    audio1 = r.listen(source1)

print(r.recognize_google(audio1))
