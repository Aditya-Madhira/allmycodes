import speech_recognition as sr
import webbrowser
import random


def converse():
    a=sr.Recognizer()
    print("1-hi   2-how are you?    3-who created you?")
    with sr.Microphone() as source:
        audio3 = a.listen(source)
        conversechoice = a.recognize_google(audio3,language='en-US')
        if conversechoice=='hi':
            print("hello")
        if conversechoice=='how are you':
            print(" i am fine.thanks for asking.i also want to ask how you are but my programmer prevents me to do so(WOW! that was long) ")
        if conversechoice=='who created you':
            print("i created myself,,,,,just kidding 'ADITYA' created me(well technically wrote me,,,wait) ")


def automate():
    b=sr.Recognizer()
    print("1-open google     2-open instagram    3-open special")
    with sr.Microphone() as source:
        audio4 = b.listen(source)
        autochoice = b.recognize_google(audio4,language='en-US')
        if autochoice=='open google':
            webbrowser.open_new_tab("https://www.google.com/")
        if autochoice=='open instagram':
            webbrowser.open_new_tab("https://www.instagram.com/accounts/login/")
        if autochoice=='open special':
            webbrowser.open_new_tab("https://www.speedtest.net/")


def jokeandfun():
    c=sr.Recognizer()
    jokes=["WHY DID THE SINGER CLIMB THE LADDER--to reach the HIGH note","WHAT HAPPENED TO PLANT IN MATH CLASS--it grew SQUARE roots"]
    facts=["there are over 6500 spoken languages in the world","the tallest man was 8ft 11in tall"]
    print("1-jokes     2-funfacts")
    with sr.Microphone() as source:
        audio5 = c.listen(source)
        jokechoice = c.recognize_google(audio5,language='en-US')
        if jokechoice=='jokes':
            dd=random.choice(list)
            print(dd)
        if jokechoice=='funfacts':
            ss=random.choice(facts)
            print(ss)


r=sr.Recognizer()
print("               WELCOME              ")
print("NOTE:PLEASE WAIT FEW SECONDS AFTER SPEAKING AND DO NOT SPEAK MULTIPLE TIMES")
print("if you dont say anything or if the computer dosen't understand it will show error,don't worry just run it again")
print("please say your name")
with sr.Microphone() as source:
    audio = r.listen(source)
    name = r.recognize_google(audio,language='en-US')
name=str(name)
name=str.capitalize(name)
print("Hello",name)
print("1-go     2-exit")
print("speak")
with sr.Microphone() as source:
        audio1 = r.listen(source)
        choice1 = r.recognize_google(audio1, language='en-US',)
        try:
          if choice1=='go':
            print("1-conversation    2-automation     3-jokes and funfacts")
            print("speak")
            with sr.Microphone() as source:
                audio2 = r.listen(source)
                choice2 = r.recognize_google(audio2,language='en-US')
                if choice2=='conversation':
                    converse()
                if choice2=='automation':
                    automate()
                if choice2=='jokes and funfacts':
                    jokeandfun()
        except:
            print("cannot understand")