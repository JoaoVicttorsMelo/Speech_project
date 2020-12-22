import pyttsx3
import speech_recognition as sr
import time as tm
import logging




speak = pyttsx3.init('sapi5')

voices = speak.getProperty('voices')
for voice in voices:
    speak.setProperty('voice', voice.id)

rate = speak.getProperty("rate")
speak.setProperty("rate", 180)

volume = speak.getProperty("volume")
speak.setProperty("volume", 1)


r = sr.Recognizer()



if __name__ == '__main__':

    while True:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            print("have a conversation with the machine: ")
            order = r.listen(source)
            try:
                Order = r.recognize_google(order, language='en-US')
                print("You said: " + Order)

                if Order == "hello":
                    tm.sleep(1)
                    speak.say("Hello, how are you?")
                    print("Hello, how are you?")
                    speak.runAndWait()

                elif Order == "hi":
                    tm.sleep(1)
                    speak.say("hi, how are you?")
                    print("hi, how are you?")
                    speak.runAndWait()

                elif Order == "stop":
                    speak.say("okay, see you later")
                    print("okay, see you later")
                    exit()

                elif Order == "I'm fine thanks how about you":
                    tm.sleep(1)
                    speak.say("I'm great thanks, how can I help?")
                    print("I'm great thanks, how can I help?")
                    speak.runAndWait()

                elif Order == "I'm fine":
                    tm.sleep(1)
                    speak.say("Very good, how can I help?")
                    speak.say("Very good, how can I help?")
                    print("I'm great thanks, how can I help?")
                    speak.runAndWait()

                elif Order == "I want to do an addition":
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


                elif Order == "I want to do a multiplication":
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

                elif Order == "I want to do a subtraction":
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

                elif Order == "I want to do a division":
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

            except Exception as e:
                logging.exception(e)
                speak.say("i don't understood")
