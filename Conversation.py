import time as tm
import pyttsx3
import speech_recognition as sr
from bs4 import BeautifulSoup
import requests
from datetime import datetime
from random import randint



r = sr.Recognizer()
speak = pyttsx3.init('sapi5')

voices = speak.getProperty('voices')
for voice in voices:
    speak.setProperty('voice', voice.id)

rate = speak.getProperty("rate")
speak.setProperty("rate", 180)

volume = speak.getProperty("volume")
speak.setProperty("volume", 1)


def conversation(word):
    with sr.Microphone() as source:

        if word == "hello":
            tm.sleep(1)
            speak.say("Hello, how are you?")
            print("Hello, how are you?")
            speak.runAndWait()

        elif word == "hi":
            tm.sleep(1)
            speak.say("hi, how are you?")
            print("hi, how are you?")
            speak.runAndWait()

        elif word == "how old you are":
            tm.sleep(1)
            age = str(randint(18, 50))
            speak.say(age)
            print(age)
            speak.runAndWait()

        elif word == "stop":
            print("okay, see you later")
            speak.say("okay, see you later")
            speak.runAndWait()
            tm.sleep(1)
            exit()

        elif word == "I'm fine thanks how about you":
            tm.sleep(1)
            speak.say("I'm great thanks, how can I help?")
            print("I'm great thanks, how can I help?")
            speak.runAndWait()

        elif word == "I'm fine":
            tm.sleep(1)
            speak.say("Very good, how can I help?")
            speak.say("Very good, how can I help?")
            print("I'm great thanks, how can I help?")
            speak.runAndWait()

        elif word == "I want to do an addition":
            speak.say("tell me the first number: ")
            print("tell me the first number: ")
            speak.runAndWait()
            num1 = r.listen(source)
            speak.say("tell me the second number: ")
            print("tell me the second number: ")
            speak.runAndWait()
            num2 = r.listen(source)
            number_1 = r.recognize_google(num1, language='en-US')
            number_2 = r.recognize_google(num2, language='en-US')
            x = int(number_1) + int(number_2)
            speak.say("the addition value is  " + str(x))
            print("the addition value is  " + str(x))
            speak.runAndWait()

        elif word == "I want to do a multiplication":
            speak.say("tell me the first number: ")
            print("tell me the first number: ")
            speak.runAndWait()
            num1 = r.listen(source)
            speak.say("tell me the second number: ")
            print("tell me the second number: ")
            speak.runAndWait()
            num2 = r.listen(source)
            number_1 = r.recognize_google(num1, language='en-US')
            number_2 = r.recognize_google(num2, language='en-US')
            x = int(number_1) * int(number_2)
            speak.say("the multiplication value is " + str(x))
            print("the multiplication value is " + str(x))
            speak.runAndWait()

        elif word == "I want to do a subtraction":
            speak.say("tell me the first number: ")
            print("tell me the first number: ")
            speak.runAndWait()
            num1 = r.listen(source)
            speak.say("tell me the second number: ")
            print("tell me the second number: ")
            speak.runAndWait()
            num2 = r.listen(source)
            number_1 = r.recognize_google(num1, language='en-US')
            number_2 = r.recognize_google(num2, language='en-US')
            x = int(number_1) - int(number_2)
            speak.say("the subtraction value is " + str(x))
            print("the subtraction value is " + str(x))
            speak.runAndWait()

        elif word == "I want to do a division":
            speak.say("tell me the first number: ")
            print("tell me the first number: ")
            speak.runAndWait()
            num1 = r.listen(source)
            speak.say("tell me the second number: ")
            print("tell me the second number: ")
            speak.runAndWait()
            num2 = r.listen(source)
            number_1 = r.recognize_google(num1, language='en-US')
            number_2 = r.recognize_google(num2, language='en-US')
            x = int(number_1) / int(number_2)
            speak.say("the division value is " + str(x))
            print("the division value is " + str(x))
            speak.runAndWait()

        elif word == "what is the weather":
            speak.say("Which country or State do you wanna Know the weather?: ")
            print("Which country do you wanna Know the weather? ")
            speak.runAndWait()
            weathers = r.listen(source)
            country = r.recognize_google(weathers, language='en-US')
            weather = requests.get('https://google.com/search?q=' + 'what is the weather in ' + country
                                   + " in fahrenheit")
            soup = BeautifulSoup(weather.content, 'html.parser')
            speak.say(soup.find('div', class_='BNeawe iBp4i AP7Wnd').text)
            print(soup.find('div', class_='BNeawe iBp4i AP7Wnd').text)
            speak.runAndWait()

        elif word == "how old is":
            speak.say("who you wanna know the age?: ")
            print("who you wanna know the age?: ")
            speak.runAndWait()
            person = r.listen(source)
            human = r.recognize_google(person, language='en-US')
            question = requests.get('https://google.com/search?q=' + 'how old is' + human)
            soup = BeautifulSoup(question.content, 'html.parser')
            age = (soup.find('div', class_='BNeawe iBp4i AP7Wnd').text.split())
            speak.say(age[0] + " Years old")
            print(age[0] + " Years old")
            speak.runAndWait()

        elif word == "what time is it":
            speak.say("Which country or State do you wanna Know the time?: ")
            print("Which country do you wanna Know the time? ")
            speak.runAndWait()
            times = r.listen(source)
            country = r.recognize_google(times, language='en-US')
            time = requests.get('https://google.com/search?q=' + 'what time is it in ' + country)
            soup = BeautifulSoup(time.content, 'html.parser')
            speak.say(soup.find('div', class_='BNeawe iBp4i AP7Wnd').text + ' o clock')
            print(soup.find('div', class_='BNeawe iBp4i AP7Wnd').text + ' o clock')
            speak.runAndWait()

        elif word == "what time is it now":
            now = datetime.now()
            current_time = now.strftime("%H:%M")
            speak.say("Current Time " + current_time)
            print("Current Time =", current_time + ' o clock')
            speak.runAndWait()

        else:
            speak.say("I wasn't prepared for this conversation, I sorry")
            print("I wasn't prepared for this conversation, I sorry")
            speak.runAndWait()


def error_msg():
    speak.say("Sorry, I don't got it")
    print("Sorry, I don't got it")
    speak.runAndWait()
