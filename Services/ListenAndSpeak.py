import speech_recognition as mic
import pyttsx3
import eel

def Speak(audio):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    rate = engine.setProperty('rate',130)
    engine.say(audio)
    print(audio)
    engine.runAndWait() 


def listening():
    status = "Wait, Starting Mic..."
    print(f"{status}")
    reco = mic.Recognizer()
    with mic.Microphone() as source:
        reco.adjust_for_ambient_noise(source)
        reco.pause_threshold = 1
        reco.energy_threshold = 300
        status = "Speak now Listening......."
        print(f"{status}")
        audio = reco.listen(source)
    try:
        print("Recognizing......")
        query = reco.recognize_google(audio, language='eng-in')
        print(f"User: {query}")
        return query.lower()
    except Exception as e:
        return 'sorry, try again, speak clearly'
    