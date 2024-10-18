import speech_recognition as sr

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("Say something...")
    
    recognizer.adjust_for_ambient_noise(source)
    audio = recognizer.listen(source)
    
try:
    command = recognizer.recognize_sphinx(audio)
    print('You said: ' + command)
    
except sr.UnknownValueError:
    print("Could not understand the audio")
    
except sr.RequestError as e:
    print(f"Request error occurred: {e}")
f

