import speech_recognition as sr

listening = True

while listening:
    with sr.Microphone() as source:
        recognizer = sr.Recognizer()
        recognizer.adjust_for_ambient_noise(source)
        recognizer.dynamic_energy_threshold = 3000
        try:
            print("listening...")
            audio = recognizer.listen(source, timeout=5.0)
            response = recognizer.recognize_google(audio)
            print(response)
        except sr.UnknownValueError:  # Fixed the typo here
            print("Didn't recognize that.")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
