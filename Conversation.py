import time as tm
import pyttsx3
import speech_recognition as sr

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

        elif word == "stop":
            print("okay, see you later")
            speak.say("okay, see you later")
            tm.sleep(3)
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
            num1 = r.listen(source)
            speak.say("tell me the second number: ")
            print("tell me the second number: ")
            num2 = r.listen(source)
            number_1 = r.recognize_google(num1, language='en-US')
            number_2 = r.recognize_google(num2, language='en-US')
            speak.say("the addition value is = ")
            print("the addition value is = ")
            x = int(number_1) + int(number_2)
            speak.say(str(x))
            print((str(x)))


        elif word == "I want to do a multiplication":
            speak.say("tell me the first number: ")
            print("tell me the first number: ")
            num1 = r.listen(source)
            speak.say("tell me the second number: ")
            print("tell me the second number: ")
            num2 = r.listen(source)
            number_1 = r.recognize_google(num1, language='en-US')
            number_2 = r.recognize_google(num2, language='en-US')
            speak.say("the multiplication value is = ")
            print("the multiplication value is = ")
            x = int(number_1) + int(number_2)
            speak.say(str(x))
            print((str(x)))

        elif word == "I want to do a subtraction":
            speak.say("tell me the first number: ")
            print("tell me the first number: ")
            num1 = r.listen(source)
            speak.say("tell me the second number: ")
            print("tell me the second number: ")
            num2 = r.listen(source)
            number_1 = r.recognize_google(num1, language='en-US')
            number_2 = r.recognize_google(num2, language='en-US')
            speak.say("the subtraction value is = ")
            print("the subtraction value is = ")
            x = int(number_1) - int(number_2)
            speak.say(str(x))
            print((str(x)))

        elif word == "I want to do a division":
            speak.say("tell me the first number: ")
            print("tell me the first number: ")
            num1 = r.listen(source)
            speak.say("tell me the second number: ")
            print("tell me the second number: ")
            num2 = r.listen(source)
            number_1 = r.recognize_google(num1, language='en-US')
            number_2 = r.recognize_google(num2, language='en-US')
            speak.say("the division value is = ")
            print("the division value is = ")
            x = int(number_1) + int(number_2)
            speak.say(str(x))
            print((str(x)))

        else:
            speak.say("I wasn't prepared for this conversation, I sorry")
            print("I wasn't prepared for this conversation, I sorry")
            speak.runAndWait()

def erromsg():
    speak.say("Sorry, I don't got it")
    print("Sorry, I don't got it")
    speak.runAndWait()