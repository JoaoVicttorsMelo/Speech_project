import speech_recognition as sr
import logging
import Conversation as Cv

if __name__ == '__main__':

    r = sr.Recognizer()
    while True:
        with sr.Microphone() as source:

            r.adjust_for_ambient_noise(source)
            print("have a conversation with the machine: ")
            order = r.listen(source)

            try:

                Order = r.recognize_google(order, language='en-US')
                print("You said: " + Order)
                Cv.conversation('how old is')


            except Exception as e:
                logging.exception(e)
                Cv.error_msg()
