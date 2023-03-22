from os import startfile
from pyautogui import click
from keyboard import press
from keyboard import press_and_release
from keyboard import write
from time import sleep
import webbrowser as web


def WhatsappMsg(name, text):
    startfile("C:\\Users\\sonia\\AppData\\Local\\WhatsApp\\WhatsApp.exe")
    sleep(5)
    click(x=165, y=160)
    sleep(3)
    write(name)
    sleep(3)
    click(x=143, y=374)
    sleep(1)
    click(x=940, y=1040)
    sleep(0.5)
    write(text)
    press('enter')


def WhatsappCall(name):
    startfile("C:\\Users\\sonia\\AppData\\Local\\WhatsApp\\WhatsApp.exe")
    sleep(5)
    click(x=165, y=160)
    sleep(3)
    write(name)
    sleep(3)
    click(x=143, y=374)
    sleep(3)
    click(x=940, y=1040)
    sleep(1)
    click(x=1551, y=93)


def WhatsappChat(name):
    startfile("C:\\Users\\sonia\\AppData\\Local\\WhatsApp\\WhatsApp.exe")
    sleep(5)
    click(x=165, y=160)
    sleep(3)
    write(name)
    sleep(3)
    click(x=143, y=374)
    sleep(3)
    click(x=940, y=1040)
    sleep(1)


def ChromeAuto(command):
    while True:
        query = str(command)
        if "new tab" in query:
            press_and_release('ctrl + t')

        elif "close tab" in query:
            press_and_release('ctrl + w')

        elif "new window" in query:
            press_and_release('ctrl + n')

        elif "history" in query:
            press_and_release('ctrl + h')

        elif "download" in query:
            press_and_release('ctrl + j')

        elif "bookmark" in query:
            press_and_release('ctrl + d')

        elif "incognito" in query:
            press_and_release('Shift + ctrl + n')

        elif "switch tab" in query:
            tab = query.replace("switch tab", "")
            Tab = tab.replace("to", "")
            num = Tab
            bb = f'ctrl + {num}'
            press_and_release(bb)

        elif 'open' in query:
            name = query.replace("open", "")
            NameA = str(name)
            if 'youtube' in NameA:
                web.open("https://www.youtube.com/")
            elif 'instagram' in NameA:
                web.open(("https://www.instagram.com/"))
            else:
                string = "https://www." + NameA + ".com"
                string_2 = string.replace(" ", "")
                web.open(string_2)

# elif "chrome" in self.query:
            #     speak("what should i search")
            #     self.query = self.takecommand().split("for")[-1]
            #     url = "https://google.com/search?q=" + self.query
            #     webbrowser.get().open(url)
            #     while True:
            #         q = self.takecommand().lower()
            #         try:
            #             if "new tab" in self.q:
            #                 press_and_release('ctrl + t')
            #
            #             elif "close tab" in self.q:
            #                 press_and_release('ctrl + w')
            #
            #             elif "new window" in q:
            #                 press_and_release('ctrl + n')
            #
            #             elif "history" in q:
            #                 press_and_release('ctrl + h')
            #
            #             elif "download" in q:
            #                 press_and_release('ctrl + j')
            #
            #             elif "bookmark" in q:
            #                 press_and_release('ctrl + d')
            #
            #             elif "incognito" in q:
            #                 press_and_release('Shift + ctrl + n')
            #
            #             elif "switch tab" in q:
            #                 tab = q.replace("switch tab", "")
            #                 Tab = tab.replace("to", "")
            #                 num = Tab
            #                 bb = f'ctrl + {num}'
            #                 press_and_release(bb)
            #
            #             elif 'open' in q:
            #                 name = q.replace("open", "")
            #                 NameA = str(name)
            #                 if 'youtube' in NameA:
            #                     webbrowser.open("https://www.youtube.com/")
            #                 elif 'instagram' in NameA:
            #                     webbrowser.open(("https://www.instagram.com/"))
            #                 else:
            #                     string = "https://www." + NameA + ".com"
            #                     string_2 = string.replace(" ", "")
            #                     webbrowser.open(string_2)
            #
            #         except Exception as e:
            #             speak(" ")

# elif "definition of" in self.query:
#     definition = self.takecommand()
#     url = urllib.request.urlopen('https://en.wikipedia.org/wiki/'+definition)
#     soup = bs4.BeautifulSoup(url, 'lxml')
#     definitions = []
#     for paragraph in soup.find_all('p'):
#         definitions.append(str(paragraph.txt))
#     if definitions:
#         if definition[0]:
#             speak('im sorry i could not find that definition')
#         elif definition[1]:
#             speak('here is what i found'+definition[1])
#         else:
#             speak('here is what i found'+definition[2])
#     else:
#         speak('im sorry i could not find that definition')

# elif "search on google" in self.query:
            #     import wikipedia as googleScrap
            #     self.query = self.query.replace("jarvis", "")
            #     self.query = self.query.replace("google search", "")
            #     self.query = self.query.replace("google", "")
            #     Speak("This is what i found on the web!")
            #
            #     try:
            #         result = googleScrap.summary(self.query,3)
            #         Speak(result)
            #
            #     except:
            #         Speak("No Speakable Data Available!")


# elif "email to sonia" in self.query:
            #     try:
            #         speak("what should i say?")
            #         content = takecommand()
            #         to = "EMAIL OF THE OTHER PERSON"
            #         sendEmail(to,content)
            #         speak("Email has been sent to avinash")

            #     except Exception as e:
            #         print(e)
            #         speak("sorry sir, i am not able to sent this mail to avi")

