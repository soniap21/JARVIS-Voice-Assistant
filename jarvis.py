import pyttsx3 # pip install pyttsx3
import pytube
import pywhatkit
import speech_recognition as sr # pip install SpeechRecognition
import datetime
import wikipedia # library to access and parse data from Wikipedia.
import webbrowserp
import wikiquotes
import os
import os.path
import requests
import cv2 # pip install opencv-python
from requests import get # pip install requests
import pywhatkit as kit # pip install opencv-python
import smtplib # pip install secure-smtplib
import pyjokes # pip install pyjokes
import pyautogui # pip install pyautogui
import PyPDF2
import json
import random
import pywikihow
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from jarvisUi import Ui_jarvisUi
import getpass
from pywikihow import search_wikihow
import sys
import time
from time import ctime
import difflib
import pyperclip
from tkinter import *
import re
from difflib import get_close_matches
import self as self
import instaloader # pip install instaloader
import operator # for calculation using voice
import psutil
import bs4
from bs4 import BeautifulSoup
from PIL import Image
from twilio.rest import Client
import speedtest
from PyDictionary import PyDictionary
from urllib import request
import urllib.request
import subprocess
from playsound import playsound
from os import startfile
from pyautogui import click
from keyboard import press
from keyboard import press_and_release
from keyboard import write
from time import sleep
import webbrowser as web
import wolframalpha
import config
from tictactoe import play
import numpy as np

data = json.load(open('C:\\Users\\sonia\\jarvisssss\\data.json'))
engine = pyttsx3.init('sapi5')  # initializes the connection and provides engine that converts text to voice
# sapi5 is a technology for voice recognition
voices = engine.getProperty('voices')  # getting details of current voice
# print(voices[0].id)
engine.setProperty('voices', voices[1].id)  # changing index, changes voices. 1 for female. 0 for female
engine.setProperty('rate', 200)

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


def wish():
    hour = int(datetime.datetime.now().hour)
    tt = time.strftime("%I:%M %p")

    if 0 <= hour <= 11:
        speak(f"good morning, its {tt}")
    elif 11 <= hour <= 18:
        speak(f"good afternoon, its {tt}")
    else:
        speak(f"good evening, its {tt}")
    speak("i am online. please tell me how may i help you")


def Time():
    t_now = datetime.datetime.now().strftime('%H:%M:%S')
    speak("The running time is")
    speak(t_now)


def text_clean(text):
    text = re.sub("\\\\", '', text)
    text = re.sub(r'\([^)]*\)', '', text)
    return text


app_id = config.wolframalpha_id


speakers = ["inspiration", "tonny robbins", "love", "life", "les brown",
            "eric thomas", "jim rohn", "brian tracy", "mel robbins"]


def DownloadYoutube():
    from pytube import YouTube
    from pyautogui import click
    from pyautogui import hotkey
    from pyperclip import paste
    from time import sleep
    sleep(2)
    click(x=1141, y=75)
    hotkey('ctrl', 'c')
    value = pyperclip.paste()
    Link = str(value)

    def Download(link):
        url = YouTube(link)
        youtube = pytube.YouTube(url)
        video = youtube.streams.first()
        video.download('C:\\Users\\sonia\\jarvisssss\\youtube')

    Download(Link)
    speak("Done, I have downloaded the video")
    speak("You can go and check it out")
    os.startfile("C:\\Users\\sonia\\jarvisssss\\youtube")


def tell_quote(how_many=1):
    quotes = wikiquotes.get_quotes(random.sample(speakers, how_many)[0], "english")
    acceptable = []

    for quote in quotes:
        length = len(quote.split(" "))
        sent = len(quote.split("."))
        if length > 5 and sent <= 10:
            acceptable.append(quote)

    getquote = random.sample(acceptable, 1)[0]
    getquote = text_clean(getquote)

    speak(getquote)


def news():
    main_url = 'http://newsapi.org/v2/top-headlines?sources=techcrunch&apikey=28a772024fce4a6399d2c76a4f2d25d1'
    # newsapi.org - api key
    main_page = requests.get(main_url).json()  # indicates that we are trying to retrieve data from specified resource.
    # print(main_page)
    articles = main_page["articles"]  # to retrieve specific data from the given source.
    # print(articles)
    head = []
    day = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range(len(day)):
        # print(f"today's {day[i]} news is: ", head[i])
        speak(f"today's {day[i]} news is:  {head[i]}")


def cpu():
    battery = psutil.sensors_battery().percent
    speak(f"Our system have {battery} percentage battery")
    if battery >= 75:
        speak("we have enough power to continue our work")
    elif 75 >= battery >= 40:
        speak("we should connect our system to the charging point")
    elif 30 >= battery >= 15:
        speak("we don't have enough power to work, please connect to charging")
    elif battery <= 15:
        speak("we have very low power, please connect to charging. The system will shut down soon.")


def Weather():
    ipAdd = requests.get('https://api.ipify.org').text
    print(ipAdd)
    url = 'https://get.geojs.io/v1/ip/geo/' + ipAdd + '.json'
    geo_requests = requests.get(url)
    geo_data = geo_requests.json()
    # print(geo_data)
    city = geo_data['city']
    api_key = "30b2e680ad9c7790ec02fdb4f97f4573"  # generate your own api key from open weather
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    city_name = (f'{city}')
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    x = response.json()
    if x["cod"] != "404":
        y = x["main"]
        current_temperature = y["temp"]
        current_pressure = y["pressure"]
        current_humidiy = y["humidity"]
        z = x["weather"]
        weather_description = z[0]["description"]
        r = ("outside " + " the Temperature is " +
             str(int(current_temperature - 273.15)) + " degree celsius " +
             ", atmospheric pressure " + str(current_pressure) + " hpa unit" +
             ", humidity is " + str(current_humidiy) + " percent"
                                                       " and " + str(weather_description))
        speak(r)
    else:
        speak(" City Not Found ")


def pdf_reader():
    book = open('guide.pdf', 'rb')  # rb = read binary # creating a pdf file object
    # creating a pdf reader object
    pdfReader = PyPDF2.PdfFileReader(book)  # PdfFileReader performs all the operations related to reading a file.
    pages = pdfReader.numPages  # counting number of pages in pdf file
    speak(f"Total numbers of pages in this book {pages}")
    speak("please enter the page number i have to read")
    pg = int(input("Please enter the page number: "))
    page = pdfReader.getPage(pg)  # creating a page object
    text = page.extractText()  # extracting text from page
    speak(text)
    # speed


class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()

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


    def run(self):
        # self.TaskExecution()
        if __name__ == "__main__":
            recognizer = cv2.face.LBPHFaceRecognizer_create()  # Local Binary Patterns Histograms
            recognizer.read('trainer/trainer.yml')  # load trained model
            cascadePath = "haarcascade_frontalface_default.xml"
            faceCascade = cv2.CascadeClassifier(cascadePath)  # initializing haar cascade for object detection approach

            font = cv2.FONT_HERSHEY_SIMPLEX  # denotes the font type

            id = 2  # number of persons you want to Recognize

            names = ['', 'sonia']  # names, leave first empty bcz counter starts from 0

            cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # cv2.CAP_DSHOW to remove warning
            cam.set(3, 640)  # set video FrameWidth
            cam.set(4, 480)  # set video FrameHeight

            # Define min window size to be recognized as a face
            minW = 0.1 * cam.get(3)
            minH = 0.1 * cam.get(4)

            # flag = True

            while True:
                ret, img = cam.read()  # read the frames using the above created object
                converted_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                # The function converts an input image from one color space to another

                faces = faceCascade.detectMultiScale(
                    converted_image,
                    scaleFactor=1.2,
                    minNeighbors=5,
                    minSize=(int(minW), int(minH)),
                )

                for (x, y, w, h) in faces:

                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)  # used to draw a rectangle on any image

                    id, accuracy = recognizer.predict(
                        converted_image[y:y + h, x:x + w])  # to predict on every single image

                    # Check if accuracy is less them 100 ==> "0" is perfect match
                    if accuracy < 100:
                        id = names[id]
                        accuracy = "  {0}%".format(round(100 - accuracy))
                        speak("verification successful")
                        press('ESC')
                        from win10toast import ToastNotifier
                        toast = ToastNotifier()
                        toast.show_toast("Jarvis", "The Jarvis Is Now Activated!", duration=3)
                        #self.TaskExecution()

                    else:
                        id = "unknown"
                        accuracy = "  {0}%".format(round(100 - accuracy))

                    cv2.putText(img, str(id), (x + 5, y - 5), font, 1, (255, 255, 255), 2)
                    cv2.putText(img, str(accuracy), (x + 5, y + h - 5), font, 1, (255, 255, 0), 1)

                cv2.imshow('camera', img)

                k = cv2.waitKey(10) & 0xff  # Press 'ESC' for exiting video
                if k == 27:
                    break

            cam.release()
            cv2.destroyAllWindows()

        while True:
            self.query = self.takecommand()
            if "wake up" in self.query:
                speak("yes, i am ready")
                wish()
                self.TaskExecution()
            elif "are you there" in self.query:
                speak("yes, i am here for you")
                wish()
                self.TaskExecution()
            elif "hello" in self.query:
                speak("hello")
                wish()
                self.TaskExecution()
            elif "goodbye" in self.query:
                speak("thanks for using me, have a good day")
                sys.exit()

    def TaskExecution(self):

        #wish()
        global time, name
        while True:
            self.query = self.takecommand()

            # logic building for tasks

            if "open notepad" in self.query:
                npath = "C:\\Windows\\system32\\notepad.exe"
                os.startfile(npath)

            elif "play song" in self.query:
                song = self.query.replace('play', '')
                speak('playing' + song)
                kit.playonyt(song)
                print(song)
                self.TaskExecution()

            elif "download this video" in self.query:
                speak("okay downloading this video")
                DownloadYoutube()

            elif 'date' in self.query:
                year = int(datetime.datetime.now().year)
                month = int(datetime.datetime.now().month)
                date = int(datetime.datetime.now().day)
                speak("the current Date is")
                speak(date)
                speak(month)
                speak(year)

            elif "open command prompt" in self.query:
                os.system("start cmd")

            elif "open whatsapp" in self.query:
                file = subprocess.Popen("C:\\Users\\sonia\\Downloads\\whatsapp.exe")

            elif "meaning" in self.query:
                speak("which word meaning do you want")
                word = self.takecommand()
                dic = PyDictionary()
                meaning = dic.meaning(word)
                speak(meaning)

            elif "weather" in self.query:
                Weather()

            elif "open camera" in self.query:
                cap = cv2.VideoCapture(0)  # return video from the first webcam on your computer.
                while True:
                    ret, img = cap.read()  # ret=return  # if img is read correctly ret is True
                    cv2.imshow('webcam', img)  # Display the resulting image
                    k = cv2.waitKey(50)  # function waitKey waits for a key event for a "delay" (here, 50 milliseconds)
                    if k == 27:  # Exit if ESC pressed # The ASCII code corresponding to ESC is 27
                        break
                cap.release()  # close video files or the capturing device
                cv2.destroyAllWindows()  # destroy the window

            elif "close camera" in self.query:
                press('ESC')

            elif "play music" in self.query:
                music_dir = "C:\\music"
                songs = os.listdir(
                    music_dir)  # listdir() returns a list containing the names music in the music folder.
                # rd = random.choice(songs)
                for song in songs:
                    if song.endswith('.mp3'):
                        os.startfile(
                            os.path.join(music_dir, song))  # os.path.join method  join one or more path components

            elif "ip address" in self.query:
                ip = get('https://api.ipify.org').text
                speak(f"your IP address is {ip}")

            elif "youtube search" in self.query:
                speak("ok, this is what i found for your search!")
                self.query = self.query.replace("jarvis", "")
                self.query = self.query.replace("youtube search", "")
                web = 'https://www.youtube.com/results?search_query=' + self.query
                webbrowser.open(web)
                speak("Done")

            elif "what is the time" in self.query or "tell me the time" in self.query:
                Time()

            elif "open youtube" in self.query:
                webbrowser.open("www.youtube.com")

            elif 'open gmail' in self.query:
                webbrowser.open("www.gmail.com")
                speak("Google Mail open now")
                time.sleep(5)

            elif "close youtube" in self.query:
                os.system("TASKKILL /F /im Chrome.exe")

            elif "close chrome" in self.query:
                os.system("TASKKILL /F /im Chrome.exe")

            elif "close the window" in self.query:
                press_and_release('alt + F4')

            elif "close whatsapp" in self.query:
                os.system("TASKKILL /F /im whatsapp.exe")

            elif "open facebook" in self.query:
                webbrowser.open("www.facebook.com")

            elif "open stack overflow" in self.query:
                webbrowser.open("www.stackoverflow.com")

            elif "open google" in self.query:
                speak("what should i search on google")
                self.query = self.takecommand().split("for")[-1]
                url = "https://google.com/search?q=" + self.query
                webbrowser.get().open(url)

            elif "search" in self.query:
                import wikipedia as googleScrap
                self.query = self.query.replace("jarvis", "")
                self.query = self.query.replace("search", "")
                self.query = self.query.replace("google", "")
                pywhatkit.search(self.query)
                speak("This is what i found on the web!")
                try:
                    result = googleScrap.summary(self.query, 2)
                    speak(result)

                except:
                    speak("No speakable data available!")

            elif "price of" in self.query:
                self.query = self.takecommand().split("for")[-1]
                url = "https://google.com/search?q=" + self.query
                webbrowser.get().open(url)
                speak("Here is what I found for " + self.query + " on google")

            elif "tweet" in self.query:
                speak("okay opening twitter...")
                import Twitterbot
                Twitterbot.tweet()

            elif "where is" in self.query:
                data = self.query.split(" ")
                location = data[2]
                speak("Hold on, I will show you where " + location + " is.")
                os.system("start chrome https://www.google.nl/maps/place/" + location)

            elif "internet speed" in self.query:
                import speedtest
                st = speedtest.Speedtest()
                dl = st.download()
                correctdl = int(dl / 800000)
                up = st.upload()
                correctup = int(up / 800000)
                speak(f"we have {correctdl} mbps downloading speed and {correctup} mbps uploading speed")

            elif "send message on whatsapp" in self.query:
                kit.sendwhatmsg("+91 87654659593", "hiii", 22, 15)
                speak("message has been sent")

            elif "whatsapp message" in self.query:
                name = self.query.replace("whatsapp message", "")
                name = name.replace("send ", "")
                name = name.replace("to ", "")
                Name = str(name)
                speak(f"Whom the message is for {Name}")
                Name = self.takecommand()
                speak(f"what is the message")
                MSG = self.takecommand()
                from Automations import WhatsappMsg
                WhatsappMsg(Name, MSG)

            elif "call" in self.query:
                from Automations import WhatsappCall
                name = self.query.replace("call ", "")
                Name = str(name)
                WhatsappCall(Name)

            elif "show chat" in self.query:
                speak("with whom?")
                name = self.takecommand()
                from Automations import WhatsappChat
                WhatsappChat(name)

            elif "you can sleep" in self.query or "sleep now" in self.query:
                speak("okay, i am going to sleep you can call me anytime.")
                break

            elif "goodbye" in self.query:
                speak("thanks for using me, have a good day")
                sys.exit()

            elif "close notepad" in self.query:
                speak("okay, closing notepad")
                os.system("taskkill /f /im notepad.exe")

            elif "set alarm" in self.query:
                speak("please tell me the time to set alarm. for example, set alarm to 5:30 a.m.")
                tt = self.takecommand()
                tt = tt.replace("set alarm to ", "")
                tt = tt.replace(".", "")
                tt = tt.upper()
                import MyAlarm
                MyAlarm.alarm(tt)
                self.TaskExecution()

            elif "wikipedia" in self.query:
                speak("searching wikipedia...")
                self.query = self.query.replace("wikipedia", "")
                results = wikipedia.summary(self.query, sentences=2)  # query said by user+sentences
                speak("according to wikipedia")
                speak(results)

            elif "tell me a joke" in self.query:
                joke = pyjokes.get_joke()
                speak(joke)

            elif "toss" in self.query or "flip" in self.query:
                moves = ["head", "tails"]
                cmove = random.choice(moves)
                speak("The computer chose " + cmove)

            elif "roll a dice" in self.query:
                while True:
                    speak("Rolling dice..")
                    number = random.randint(1, 6)
                    speak(f"your number is {number}")
                    speak("Do you want to roll the dice again? Yes or No")
                    choice = self.takecommand()
                    if "no" in choice:
                        break

            elif "shut down the system" in self.query:
                speak("do you really want to shutdown")
                reply = self.takecommand()
                if "yes" in reply:
                    os.system("shutdown /s /t 5")
                else:
                    break

            elif "restart the system" in self.query:
                speak("do you really want to restart")
                reply = self.takecommand()
                if "yes" in reply:
                    os.system("shutdown /r /t 5")
                else:
                    break

            elif "sleep the system" in self.query:
                speak("do you really want to make system sleep")
                reply = self.takecommand()
                if "yes" in reply:
                    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
                else:
                    break

            elif "write down something" in self.query:
                speak("what should i write down")
                note = self.takecommand()
                remember = open("data.txt", 'w')
                remember.write(note)
                remember.close()
                speak("I have noted that " + note)

            elif "do you remember anything" in self.query:
                remember = open('data.txt', 'r').read()
                speak("You told me to remember that  " + remember)

            elif "hello" in self.query or "hey" in self.query:
                speak("hello, may i help you with something.")

            elif "how are you" in self.query:
                speak("i am fine, what about you.")

            elif "i am good" in self.query:
                speak("good to hear that, have a nice day.")

            elif "thank you" in self.query or "thanks" in self.query:
                speak("it's my pleasure.")

            elif 'switch the window' in self.query:
                pyautogui.keyDown("alt")
                pyautogui.press("tab")
                time.sleep(1)
                pyautogui.keyUp("alt")

            elif "tell me news" in self.query:
                speak("please wait, fetching the latest news")
                news()

            elif "do some calculations" in self.query or "can you calculate" in self.query:
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    speak("Say what you want to calculate, example: 3 plus 3")
                    print("listening.....")
                    r.adjust_for_ambient_noise(source)
                    audio = r.listen(source)
                my_string = r.recognize_google(audio)
                print(my_string)

                def get_operator_fn(op):
                    return {
                        '+': operator.add,
                        '-': operator.sub,
                        'x': operator.mul,
                        'divided': operator.__truediv__,
                        'Mod': operator.mod,
                        'mod': operator.mod,
                        '^': operator.xor,
                    }[op]

                def eval_binary_expr(op1, oper, op2):
                    op1, op2 = int(op1), int(op2)
                    return get_operator_fn(oper)(op1, op2)

                print(eval_binary_expr(*(my_string.split())))

            elif "where am i" in self.query or "where are we" in self.query:
                speak("wait, let me check")
                try:
                    ipAdd = requests.get('https://api.ipify.org').text
                    print(ipAdd)
                    url = 'https://get.geojs.io/v1/ip/geo/' + ipAdd + '.json'
                    geo_requests = requests.get(url)
                    geo_data = geo_requests.json()
                    # print(geo_data)
                    city = geo_data['city']
                    # state = geo_data['state']
                    country = geo_data['country']
                    speak(f"i am not sure, but i think we are in {city} city of {country} country")
                except Exception as e:
                    speak("sorry, Due to network issue i am not able to find where we are.")
                    self.TaskExecution()

            elif "instagram profile" in self.query or "profile on instagram" in self.query:
                speak("please enter the user name correctly.")
                name = input("Enter username here:")
                webbrowser.open(f"www.instagram.com/{name}")
                speak(f"here is the profile of the user {name}")
                time.sleep(5)
                speak("would you like to download profile picture of this account.")
                condition = self.takecommand()
                if "yes" in condition:
                    mod = instaloader.Instaloader()  # pip install instadownloader
                    mod.download_profile(name, profile_pic_only=True)
                    speak("i am done, profile picture is saved in our main folder. now i am ready for next command")
                else:
                    self.TaskExecution()

            elif "take screenshot" in self.query or "take a screenshot" in self.query:
                speak("tell me the name of this screenshot file")
                name = self.takecommand().lower()
                speak("please hold the screen for few seconds, i am taking screenshot")
                time.sleep(2)
                img = pyautogui.screenshot()
                img.save(f"C:\\Users\\sonia\\jarvisssss\\screenshots\\{name}.png")
                speak("i am done, the screenshot is saved in the main folder")
                speak("Do you want to see the screenshot?")
                ss = self.takecommand()
                if "yes" in ss:
                    try:
                        img.show(f"C:\\Users\\sonia\\jarvisssss\\screenshots\\{name}.png")
                        speak("Here it is.")
                        time.sleep(2)
                    except IOError:
                        speak("Sorry, I am unable to display the screenshot")
                        self.TaskExecution()
                else:
                    self.TaskExecution()

            elif "close it" in self.query:
                press_and_release('alt+F4')

            elif "game" in self.query:
                speak("okay, lets play rock paper scissors")
                while True:
                    speak("choose among rock paper or scissor")
                    ans = self.takecommand()
                    try:
                        if "exit" in ans or "close" in ans:
                            speak("okay, game is closed")
                            break

                        else:
                            moves = ["rock", "paper", "scissor"]
                            cmove = random.choice(moves)
                            pmove = ans

                            speak("I choose " + cmove)
                            speak("You chose " + pmove)
                            if pmove == cmove:
                                speak("the match is draw")
                            elif pmove == "rock" and cmove == "scissor":
                                speak("you win")
                            elif pmove == "rock" and cmove == "paper":
                                speak("I won")
                            elif pmove == "paper" and cmove == "rock":
                                speak("you win")
                            elif pmove == "paper" and cmove == "scissor":
                                speak("I won")
                            elif pmove == "scissor" and cmove == "paper":
                                speak("you win")
                            elif pmove == "scissor" and cmove == "rock":
                                speak("I won")
                    except Exception as e:
                        speak("sorry, i am not able to find this")

            elif "read pdf" in self.query:
                pdf_reader()

            elif 'your name' in self.query:
                speak('My name is JARVIS')

            elif 'stand for' in self.query:
                speak('J.A.R.V.I.S stands for JUST A RATHER VERY INTELLIGENT SYSTEM')

            elif "battery" in self.query or "power" in self.query:
                cpu()

            elif 'search' in self.query:
                query = self.query.replace("search", "")
                speak('searching' + query)
                webbrowser.open(query)
                time.sleep(3)

            elif "voice" in self.query:
                if 'female' in self.query:
                    engine.setProperty('voice', voices[0].id)
                else:
                    engine.setProperty('voice', voices[1].id)
                speak("Hello, I have switched my voice. How is it?")
                speak("Did you like it?")
                condition = self.takecommand()
                if "yes" in condition:
                    speak("thank you!")
                elif "no" in condition:
                    speak("oh okay, i am sad now")

            elif 'inspirational quote' in self.query:
                tell_quote()

            elif 'temperature' in self.query:
                search = "temperature in kalyan"
                url = f"https://www.google.com/search?q={search}"
                r = requests.get(url)
                data = BeautifulSoup(r.text, "html.parser")
                temp = data.find("div", class_="BNeawe").text
                speak(f"current {search} is {temp} ")

            elif "weather outside" in self.query:
                print("searching...")
                Weather()

            elif "volume up" in self.query:
                pyautogui.press("volumeup")

            elif "volume down" in self.query:
                pyautogui.press("volumedown")

            elif "mute" in self.query:
                pyautogui.press("volumemute")

            elif "open mobile camera" in self.query:
                import numpy as np
                import time
                import urllib.request
                URL = "http://192.168.0.180:8080/shot.jpg"
                while True:
                    img_arr = np.array(bytearray(urllib.request.urlopen(URL).read()), dtype=np.uint8)
                    img = cv2.imdecode(img_arr, -1)
                    cv2.imshow('IPWebcam', img)
                    q = cv2.waitKey(1)
                    if q == ord("q"):
                        break

            elif "find location" in self.query:
                speak("what is the location?")
                location = self.takecommand()
                url = 'https://google.nl/maps/place/' + location + '/&amp;'
                webbrowser.get().open(url)
                speak('here is the location of' + location)

            elif "activate how to do" in self.query:
                speak("How to do mode is activated")
                while True:
                    speak("Please tell me what you want to know")
                    how = self.takecommand()
                    try:
                        if "exit" in how or "close" in how:
                            speak("okay, how to do mode is closed")
                            self.TaskExecution()
                        else:
                            max_results = 1
                            how_to = pywikihow.search_wikihow(how, max_results)
                            assert len(how_to) == 1
                            how_to[0].print()
                            speak(how_to[0].summary)
                    except Exception as e:
                        speak("sorry, i am not able to find this")
                        self.TaskExecution()

            elif "activate dictionary" in self.query:
                speak("Activated dictionary!")
                dictionary = PyDictionary()
                while True:
                    speak("Tell me the problem!")
                    prob1 = self.takecommand()
                    try:
                        if "no" in prob1 or "exit" in prob1:
                            speak("Exited dictionary")
                        else:
                            if 'meaning of' in prob1:
                                prob1 = prob1.replace("meaning of", "")
                                result = dictionary.meaning(prob1)
                                speak(f"The meaning for {prob1} is {result}")

                    except Exception as e:
                        speak("sorry, i am not able to find this")

            elif "pause" in self.query:
                press("space bar")

            elif "restart" in self.query:
                press('0')

            elif "mute" in self.query:
                press('m')

            elif "skip" in self.query:
                press('l')

            elif "normal" in self.query:
                press('ESC')

            elif "back" in self.query:
                press('j')

            elif "full screen" in self.query:
                press('f')

            elif "full mode" in self.query:
                press('t')

            elif "play" in self.query:
                press('space bar')

            elif "unmute" in self.query:
                press('m')

            elif "new tab" in self.query:
                press_and_release('ctrl + t')

            elif "close tab" in self.query:
                press_and_release('ctrl + w')

            elif "new window" in self.query:
                press_and_release('ctrl + n')

            elif "history" in self.query:
                press_and_release('ctrl + h')

            elif "download" in self.query:
                press_and_release('ctrl + j')

            elif "bookmark" in self.query:
                press_and_release('ctrl + d')

            elif "incognito" in self.query:
                press_and_release('Shift + ctrl + n')

            elif "switch tab" in self.query:
                press_and_release('alt + tab')

            elif 'open' in self.query:
                name = self.query.replace("open", "")
                NameA = str(name)
                if 'youtube' in NameA:
                    webbrowser.open("https://www.youtube.com/")
                elif 'instagram' in NameA:
                    webbrowser.open("https://www.instagram.com/")
                else:
                    string = "https://www." + NameA + ".com"
                    string_2 = string.replace(" ", "")
                    webbrowser.open(string_2)

            elif "tic tac toe" in self.query:
                speak("okay opening game..")
                play()


cv2.destroyAllWindows()


startExecution = MainThread()


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_jarvisUi()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)

    def startTask(self):
        self.ui.movie = QtGui.QMovie("output-onlinegiftools-2--unscreen.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("output-onlinegiftools (1).gif")
        self.ui.label_4.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("output-onlinegiftools-2--unscreen.gif")
        self.ui.label_5.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()

    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString('hh:mm:ss')
        label_date = current_date.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser_2.setText(label_time)

import sys
app = QApplication(sys.argv)
jarvis = Main()
jarvis.show()
exit(app.exec_())