from email import encoders
from email.message import EmailMessage
from email.mime.base import MIMEBase
from msilib.text import UIText
import operator
import time
import geocoder
# from typing import Self
import PyPDF2
from click import BaseCommand
import instaloader
import pypdf
import pyttsx3
import requests
import speech_recognition as sr
import datetime
import os
import cv2
import random
from requests import get
import wikipedia
import webbrowser
# import pywhatkit as kit
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import instaloader
import sys
import pyjokes
import pyautogui 
import PyPDF2
from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.QtCore import QTimer,QTime,QDate,Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from jarvisui1 import Ui_MainWindow
from bs4 import BeautifulSoup
import numpy as np
import operator
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voices',voices[0].id)
# Speak Fuction
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


def closesysapplication(app_name):
    os.system(f"TASKKILL /F /IM {app_name}.exe")
# 
def close_application():
    pyautogui.hotkey('ctrl', 'w')
#Wish fuction to wish  

def wish():
    hour=int(datetime.datetime.now().hour)
    if hour >=0 and hour <= 12:
       
        jarvis.printToTerminal ("good morning") 
        speak("Good morning")
    if hour >12 and hour < 18:
        jarvis.printToTerminal ("good afternoon") 
        speak("Good Afternoon")
    else:
        jarvis.printToTerminal ("good evinig") 
        speak("Good Eveinig")
        jarvis.printToTerminal ("I am Jarvis sir...How Can I help You sir") 
    speak("I am Jarvis sir...How Can I help You sir")




def news():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Please say the category for the news")
        jarvis.printToTerminal("Please say the category for the news")
        audio=r.listen(source)
        speak("Plz wai sir , fetching the latest news")
        jarvis.printToTerminal("Plz wai sir , fetching the latest news")
        
    try:
        category=r.recognize_google(audio)
    except Exception as e:
        print("Error: " + str(e))
        return
    
    main_url=f'https://newsapi.org/v2/top-headlines?category={category}&apiKey=8f5c9bcf562f437d84ade5742b6353b6'

    main_page=requests.get(main_url).json()
    articles=main_page["articles"]
    head=[]
    for ar in articles[:5]:
        head.append(ar["title"])
    speak(f"Here are the top news in {category} today: ")
    jarvis.printToTerminal(f"Here are the top news in {category} today: ")
    for i in range(len(head)):
        speak(f"Today's {i+1} news is: {head[i]}")
        jarvis.printToTerminal(f"Today's {i+1} news is: {head[i]}")

# pdf read fuction

def pdf_read():
    book=open("OOPS in Java.pdf",'rb')
    pdfreader = PyPDF2.PdfReader(book)
    pages = len(pdfreader.pages)
    speak("Toal pages in pdf is {pages}")

    speak("sir plz enter the page no i have to read :")
    pg=int(input("plz enter the page number :"))
    page=pypdf.PdfReader.GetPage(pg)
    text=page.extractText()
    speak(text)

# main thread to execute all operations

class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()
    
    def run(self):
        # self.TaskExecution().lower()
        jarvis.printToTerminal("I am Jarvis sir...How Can I help You sir") 
        
        speak("plz say wakup to continue")
        while True:
            self.query=self.TakeCommand()
            if "wake up" in self.query or "are you there" in self.query or "hello" in self.query:
                self.TaskExecution().lower()

# User inpute command

    def TakeCommand(self):

        r = sr.Recognizer()

        with sr.Microphone() as source:
        
            jarvis.printToTerminal("Jarvis :Listening......") 
            

            r.pause_threshold = 1

            audio = r.listen(source)


        try:

            jarvis.printToTerminal ("recognizing....") 
          

            query = r.recognize_google(audio,language='en-in')

            print(f": Your Command : {query}\n")
            jarvis.printToTerminal (f"your Command :{query}") 

        except:
            return ""

        return query.lower()

# Task execute ladder

    def TaskExecution(self):
        wish()
        while True:
            self.query=self.TakeCommand().lower()
            
 #Open note pad here
             
            if "open notepad"  in self.query:
                path="C:\\Windows\\notepad.exe"
                os.startfile(path)
            # close notepad

            elif "close notepad" in self.query:
                speak("okey sir , closing....")
                closesysapplication("notepad")
            
# Open cmd

            elif "open cmd" in self.query:
                os.system("Start cmd") 
                
            elif "close cmd" in self.query:
                speak("okey sir , closing....")
                closesysapplication("cmd")

# Open camera

            elif "camera" in self.query:
                cap=cv2.VideoCapture(0)
                while True:
                    ret,img=cap.read()
                    cv2.imshow('webcam',img)
                    k=cv2.waitKey(50)
                    if k==27:
                        break
                cap.release()
                cv2.destroyAllWindows()
                
            elif "close camera" in self.query:
                speak("okey sir , closing....")
                closesysapplication("WindowsCamera")

 # Play music

            elif "play music" in self.query:
                    music_dir="C:\\Users\\SAMBHAJI\\Music"
                    songs=os.listdir(music_dir)
                    # rd=random.choice(songs)
                    os.startfile(os.path.join(music_dir,songs[0]))
            
 # To find IP Addr

            elif "IP address" in self.query:
                ip = requests.get('https://api.ipify.org').text
                speak(f"Your IP address is {ip}.")

 # Search on wikipedia

            elif "wikipedia" in self.query:
                    speak("Searching wikipedia....")
                    query=self.query.replace("wikipedia","")
                    results=wikipedia.summary(query,sentences=2)
                    speak("According to wikipedia..")
                    speak(results)
            elif "close facebook" in self.query:
                speak("Closing facebook")
                close_application()

 # Open Youtube
            elif  "open youtube" in self.query:
                speak("sir, what should I search on YouTube?")
                cm = self.TakeCommand().lower()
                webbrowser.open(f"https://www.youtube.com/results?search_query={cm}")
            elif "close youtube" in self.query:
                speak("Closing YouTube")
                close_application()

 # Open Facebook

            elif "open facebook" in self.query:
                webbrowser.open("www.facebook.com")
            elif "close facebook" in self.query:
                speak("Closing facebook")
                close_application()

            
 # open google

            elif "open google" in self.query:
                speak("sir, what should i search on google")
                cm=self.TakeCommand().lower()
                webbrowser.open(f"{cm}")
            elif "close google" in self.query:
    # Close the YouTube tab by closing the active window
                speak("Closing google")
                close_application()
 
            
            elif "open notepad"  in self.query:
                path="C:\\Windows\\notepad.exe"
                os.startfile(path)
            
 # Send emial

            elif "email" in self.query:
                speak("What should I say?")
                message_content = self.TakeCommand().lower()

                # Set up the email parameters
                email = EmailMessage()
                email['From'] = 'sayyadshahrukh2000@gmail.com'
                email['To'] = 'sayyadshahrukh2250@gmail.com'
                email['Subject'] = 'Testing'
                email.set_content(message_content)

                if "send a file" in self.query:
                    # Get the file path from the user
                    speak("please enter path to send file")
                    file_path = input().strip()

                    # Attach the file to the email
                    with open(file_path, 'rb') as f:
                        file_data = f.read()
                        file_name = os.path.basename(file_path)
                    email.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

                # Send the email
                with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                    smtp.login('sayyadshahrukh2000@gmail.com', 'shan@niks1727')
                    smtp.send_message(email)

                # Speak confirmation message
                speak("Email sent successfully!")
                        
 
#Sending Message 
            elif "send message" in self.query:
                # SMS.SmsSend()
                from twilio.rest import Client

                speak("sir what would i say ")
                jarvis.printToTerminal("Sir what would i say ")
                
                msg=self.TakeCommand().lower()
                speak("Sending messege")

                account_sid ='AC38915a5f031e8766da07c4039264e2e7'
                auth_token = '2270f8cdd20f6a96d7c23ba233ce1cf8'
                client = Client(account_sid, auth_token)

                message = client.messages \
                    .create(
                        body=msg,
                        from_='+16203613859',
                        to='+919322984458'
                    )

                print(message.sid)

 # Set alarm

            elif "set alarm" in self.query:
                speak("tell me time to set alarm")
                nn=int(datetime.datetime.now().hour)
                if nn==22:
                    music_dir="C:\\Users\\SAMBHAJI\\Music"
                    songs=os.listdir(music_dir)
                    os.startfile(os.path.join(music_dir,songs[0]))

# Jokes

            elif "tell me joke" in self.query:
                jokes = pyjokes.get_jokes()
                for joke in jokes[:5]:  # Get the first five jokes from the list
                    speak(joke)
                    jarvis.printToTerminal(joke)


# Shutdown pc 

            elif "shut down system" in self.query:
                speak("Okay sir, shutting down.")
                os.system("shutdown /s /t 0")


# Restart pc

            elif "restart" in self.query:
                speak("Okay sir, restarting.")
                os.system("shutdown /r /t 0")


# Sleep pc

            elif "sleep system" in self.query:
             os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

 # switch another window

            elif "window" in self.query:
                pyautogui.keyDown("alt")
                pyautogui.press("tab")
                pyautogui.keyUp("alt")
            
# News

            elif "tell me news" in self.query:
                news()


            elif "no thanks" in self.query:
                speak("thank u for using me,have a good day sir")
                sys.exit()

 # Find Your Location 

            elif "where i am" in self.query:
                    speak("Wait sir let me check..")
                    try:
                        # Get the public IP address of the device
                        ipAdd = requests.get('https://api.ipify.org').text
                        print(ipAdd)

                        # Get the geo location data using the IP address
                        url = 'http://get.geojs.io/v1/ip/geo/' + ipAdd + '.json'
                        geoRequests = requests.get(url)
                        geoData = geoRequests.json()
                        city = geoData['city']
                        country = geoData['country']

                        # Speak the location
                        speak(f"Sir, I think we are in {city} city of {country} country.")
                        jarvis.printToTerminal(f"Sir, I think we are in {city} city of {country} country.")
                    except Exception as e:
                        speak("Sorry sir, due to a network issue, I am not able to find where we are.")

# To find instagram profile

            elif "instagram profile" in self.query:
                speak("Sir enter the user name correctly")
                name=input("Enter user name here :")
                webbrowser.open(f"www.instagram.com/{name}")
                speak((f"sir here is the profile of user {name}"))
                time.sleep(5)
                speak("Sir would you like to download this profile picture say download to download")
                jarvis.printToTerminal("Sir would you like to download this profile picture say download to download")

                condition=self.TakeCommand().lower()
                if "download" in condition:
                    mod=instaloader.Instaloader()
                    mod.download_profile(name,profile_pic_only=True)
                    speak("I am done sir, profile pic save our main folder. now i am ready")
                    jarvis.printToTerminal("I am done sir, profile pic save our main folder. now i am ready")

                else:
                    pass
            elif "close insta" in self.query:
                speak("Closing instagram")
                close_application()
            
# TO take screenshot

            elif "snapshot" in self.query:
                speak("Sir , plz tell me name for this screenshot file")
                name=self.TakeCommand().lower()
                speak("plz holding the screenshot for few second iam taking screenshot")
                time.sleep(5)
                img=pyautogui.screenshot()
                img.save(f"{name}.png")
                speak("i am done sir, the screenshot is saved in our main folder")
            

 # To read pdf

            elif "read pdf" in self.query:
                pdf_read()

# to hide or unhide file

            elif "file" in self.query or "visible" in self.query:
                speak("Sir, please tell me do you want to hide this folder or make it visible to everyone.")
                condition = self.TakeCommand().lower()
                if "hide" in condition:
                    os.system("attrib +h /s /d <JARVIS_NEW>")
                    speak("This folder is now hidden, sir.")
                elif "visible" in condition:
                    os.system("attrib -h /s /d <folder_path>")
                    speak("This folder is now visible to everyone, sir.")

            
# Do calculations
                elif "calculations" in self.query or "calculate" in self.query:
                    try:
                        r = sr.Recognizer()
                        with sr.Microphone() as source:
                            speak("Which calculation you want to do, sir? For example, say '3 plus 3'.")
                            print("Listening...")
                            r.adjust_for_ambient_noise(source)
                            audio = r.listen(source)
                        my_string = r.recognize_google(audio)
                        print(my_string)
                        
                        def get_operator_fn(op):
                            return{
                                '+': operator.add,
                                '-': operator.sub,
                                '*': operator.mul,
                                'divided': operator.__truediv__,
                            }[op]
                        
                        def eval_binary_expr(op1, oper, op2):
                            op1, op2 = int(op1), int(op2)
                            return get_operator_fn(oper)(op1, op2)
                        
                        result = eval_binary_expr(*(my_string.split()))
                        speak(f"Your result is {result}")
        
                    except Exception as e:
                        print(e)
                        speak("Sorry sir, I could not understand that calculation.")


            elif "temperature" in self.query:
                search = "temperature in pune"
                url = f"https://www.google.com/search?q={search}"
                r = requests.get(url)
                data = BeautifulSoup(r.text, "html.parser")
                temp = data.find("div", class_="BNeawe iBp4i AP7Wnd").text
                speak(f"The current {search} is {temp}")
                jarvis.printToTerminal(f"The current {search} is {temp}")


# object of main thread
startExecution=MainThread()

# main class

class Main(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)
# Task execute by gui 
    def startTask(self):
        # self.ui.movie=QtGui.QMovie("jarvis1.gif")
        # self.ui.label_2.setMovie(self.ui.movie)
        # self.ui.movie.start()
        self.ui.movie=QtGui.QMovie("FronEnd_img/jar1.gif")
        self.ui.label_3.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie=QtGui.QMovie("FronEnd_img/bot.gif")
        self.ui.label_4.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie=QtGui.QMovie("FronEnd_img/nova.gif")
        self.ui.label_5.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie=QtGui.QMovie("FronEnd_img/r.gif")
        self.ui.label_6.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer=QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()
# date time fuction on gui
    def showTime(self):
        curruent_time=QTime.currentTime()
        currurent_date=QDate.currentDate()
        currurent_date=QDate.currentDate()
        lable_time=curruent_time.toString('hh:mm:ss')
        lable_date=currurent_date.toString(Qt.ISODate)
        self.ui.textBrowser.setText(lable_date)
        self.ui.textBrowser_2.setText(lable_time)

    def printToTerminal(self, text):
        self.ui.terminal_outpu.appendPlainText(text)
        

app=QApplication(sys.argv)

jarvis=Main()

jarvis.show()

#exit(app.exec_())


