import pyttsx3
import speech_recognition as sr
import time as tm

speak = pyttsx3.init('sapi5')
r = sr.Recognizer()
while True:

    with sr.Microphone() as source:

        print("have a conversation with the machine: ")
        order = r.listen(source)
        try:
            Order = r.recognize_google(order, language='eng-EUA')
            speak.say('Your order was: ' + Order)

            if Order == "hello":
                tm.sleep(1)
                speak.say("Hello, how are you?")
                speak.runAndWait()

            if Order == "I'm fine thanks how about you":
                tm.sleep(1)
                speak.say("I'm great thanks, how can I help?")
                speak.runAndWait()

            if Order == "I want to do an addition":
                speak.say("tell me the first number: ")
                num1 = r.listen(source)
                speak.say("tell me the second number: ")
                num2 = r.listen(source)
                number_1 = r.recognize_google(num1, language='eng-EUA')
                number_2 = r.recognize_google(num2, language='eng-EUA')
                speak.say("the addition value is = ")
                x = int(number_1) + int(number_2)
                speak.say(str(x))

            if Order == "I want to do a multiplication":
                speak.say("tell me the first number: ")
                num1 = r.listen(source)
                speak.say("tell me the second number: ")
                num2 = r.listen(source)
                number_1 = r.recognize_google(num1, language='eng-EUA')
                number_2 = r.recognize_google(num2, language='eng-EUA')
                speak.say("the multiplication value is = ")
                x = int(number_1) + int(number_2)
                speak.say(str(x))

            if Order == "I want to do a subtraction":
                speak.say("tell me the first number: ")
                num1 = r.listen(source)
                speak.say("tell me the second number: ")
                num2 = r.listen(source)
                number_1 = r.recognize_google(num1, language='eng-EUA')
                number_2 = r.recognize_google(num2, language='eng-EUA')
                speak.say("the subtraction value is = ")
                x = int(number_1) + int(number_2)
                speak.say(str(x))
            if Order == "I want to do a division":
                speak.say("tell me the first number: ")
                num1 = r.listen(source)
                speak.say("tell me the second number: ")
                num2 = r.listen(source)
                number_1 = r.recognize_google(num1, language='eng-EUA')
                number_2 = r.recognize_google(num2, language='eng-EUA')
                speak.say("the division value is = ")
                x = int(number_1) + int(number_2)
                speak.say(str(x))
        except:
            speak.say("i don't understood")
