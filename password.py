import pyttsx3
import speech_recognition as sr
from win10toast import ToastNotifier

engine = pyttsx3.init('sapi5')  # initializes the connection and provides engine that converts text to voice
# sapi5 is a technology for voice recognition
voices = engine.getProperty('voices')  # getting details of current voice
# print(voices[0].id)
engine.setProperty('voices', voices[1].id)  # changing index, changes voices. 1 for female. 0 for female
engine.setProperty('rate', 200)


def Pass(pass_inp):
    password = "python"
    passs = str(password)
    if passs == str(pass_inp):
        speak("Assess Granted")
        import jarvis
    else:
        speak("Access not granted")


def takecommand(self):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        # r.adjust_for_ambient_noise(source)
        # audio = r.listen(source)
        audio = r.listen(source, timeout=5, phrase_time_limit=7)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")

    except sr.UnknownValueError:
        print('I did not get that')
        self.TaskExecution()

    except sr.RequestError:
        speak('Sorry, the service is down')

    except Exception as e:
        speak("Say that again please...")
        return "none"
    query = query.lower()
    return query


def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


def Pass(pass_inp):
    password = "python"
    passs = str(password)
    if passs == str(pass_inp):
        speak("Assess Granted")
        from jarvis import MainThread
    else:
        speak("Access not granted")



