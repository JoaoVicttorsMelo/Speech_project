import speech_recognition as sr
import time as tm

i = 0

while i == 0:
    r = sr.Recognizer()
    with sr.Microphone() as source:

        print("have a conversation with the machine: ")
        order = r.listen(source)
        try:
            Order = r.recognize_google(order, language='eng-EUA')
            print('Your order was: ' + Order)

            if Order == "hello":
                tm.sleep(1)
                print("Hello, how are you?")

            if Order == "I'm fine thanks how about you":
                tm.sleep(1)
                print("I'm great thanks, how can I help?")

            if Order == "I want to do an addition":
                print("tell me the first number: ")
                num1 = r.listen(source)
                print("tell me the second number: ")
                num2 = r.listen(source)
                number_1 = r.recognize_google(num1, language='eng-EUA')
                number_2 = r.recognize_google(num2, language='eng-EUA')
                print("the addition value is = ")
                print(int(number_1) + int(number_2))

            if Order == "I want to do a multiplication":
                print("tell me the first number: ")
                num1 = r.listen(source)
                print("tell me the second number: ")
                num2 = r.listen(source)
                number_1 = r.recognize_google(num1, language='eng-EUA')
                number_2 = r.recognize_google(num2, language='eng-EUA')
                print("the multiplication value is = ")
                print(int(number_1) * int(number_2))

            if Order == "I want to do a subtraction":
                print("tell me the first number: ")
                num1 = r.listen(source)
                print("tell me the second number: ")
                num2 = r.listen(source)
                number_1 = r.recognize_google(num1, language='eng-EUA')
                number_2 = r.recognize_google(num2, language='eng-EUA')
                print("the subtraction value is = ")
                print(int(number_1) - int(number_2))

            if Order == "I want to do a division":
                print("tell me the first number: ")
                num1 = r.listen(source)
                print("tell me the second number: ")
                num2 = r.listen(source)
                number_1 = r.recognize_google(num1, language='eng-EUA')
                number_2 = r.recognize_google(num2, language='eng-EUA')
                print("the division value is = ")
                print(int(number_1) / int(number_2))

        except:
            print("...")
