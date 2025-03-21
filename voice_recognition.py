import speech_recognition as sr

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    
    try:
        command = recognizer.recognize_google(audio).lower()
        print(f"Recognized: {command}")
        return command
    except sr.UnknownValueError:
        return None

if __name__ == "__main__":
    print(recognize_speech())
