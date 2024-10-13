import speech_recognition as sr

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print ("say sum")
    audio = recognizer.listen(source)
    
try:
    command = recognizer.recognize_sphinx(audio)
    print ('you said:' + command)
except sr.UnknownValueError:
    print ('cant understand')
except sr.RequestError as e:
    print("error" + e)