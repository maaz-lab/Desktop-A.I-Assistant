import os
import sys
import wikipedia
import speech_recognition as sr
import win32com.client
import webbrowser
import openai
import datetime
import requests
from playsound import playsound
from pydub import AudioSegment
from pydub.playback import play

speaker = win32com.client.Dispatch("SAPI.Spvoice")


def say(Text):
    speaker.Speak(Text)


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:

        audio = r.listen(source)
        try:
            print("Recognizing....")
            query = r.recognize_google(audio, language="en-pk")
            print("User Query : ",query)
            return query
        except Exception as e:
            return ""

if __name__ == '__main__':
    say("Hello I am Maaz A.I")
    while True:
        print("Listening....")
        query = takecommand()

        sites = [["youtube","https://www.youtube.com/"],["google","https://www.google.com/"],["netflix","https://www.netflix.com/"],["facebook","https://www.facebook.com/"],["wikipedia","https://www.wikipedia.org/"],["github","https://github.com/explore"], ["linkedin","https://www.linkedin.com/"],["instagram","https://www.instagram.com/"],["yahoo","https://www.yahoo.com/"],["whatsapp","https://www.whatsapp.com/"]]
        for site in sites:
            if "open "+site[0]+"".lower() in query.lower():
                webbrowser.open(site[1])
                say("Opening"+site[0]+ "Sir")

        if "Thank you".lower() in query.lower():
            say("Your Welcome Sir")
        elif "How are you".lower() in query.lower():
            say("i am fine thankyou for asking")
        elif "joke".lower() in query.lower():
             limit = 1
             #API for generating jokes
             api_url = 'https://api.api-ninjas.com/v1/jokes?limit={}'.format(limit)
             response = requests.get(api_url, headers={'X-Api-Key': 'q3SJ8bRy2wTo+DF5TbrHjA==Y6ZDrxfMbl9wcxFT'})
             if response.status_code == requests.codes.ok:
                 print(response.text)
                 say(response.text)
                 song = AudioSegment.from_wav("maled.wav")
                 play(song)
                 #playsound('C:/Users/MAAZ ALI KHAN/Downloads/ppp.mp3')
             else:
                 print("Error:", response.status_code, response.text)
        elif "Generate a random password".lower() and "random pass".lower() and "random password".lower() in query.lower():
            length = '10'
            #API for generating a random password
            api_url = 'https://api.api-ninjas.com/v1/passwordgenerator?length={}'.format(length)
            response = requests.get(api_url, headers={'X-Api-Key': 'q3SJ8bRy2wTo+DF5TbrHjA==Y6ZDrxfMbl9wcxFT'})
            if response.status_code == requests.codes.ok:
                print(response.text)
            else:
                print("Error:", response.status_code, response.text)
        elif "Hello".lower() in query.lower():
            say("Hello Sir How may I Help You")
        elif "Bye".lower() in query.lower():
            say("Bye Bye")
            break
        elif "Shut Up".lower() and "Fuck off".lower() in query.lower():
            say("You are so rude!!!")
            break
        elif "open music".lower() in query.lower():
            os.startfile('C:/Users/MAAZ ALI KHAN/Downloads/music1234.mp4')
        elif "the time".lower() in query.lower():
            Hours = datetime.datetime.now().strftime("%H")
            minutes = datetime.datetime.now().strftime("%M")
            say("The time is "+Hours+" Hours and "+minutes+" minutes ")
        elif "Who are you".lower() in query.lower():
            say("I am an A I model and my name is Maaz.AI")
        elif "what is your name".lower() in query.lower():
            say("I am an A.I model and my name is Maaz.AI")
        elif "give me your identification".lower() in query.lower():
            say("I am an A.I model and my name is Maaz.AI")
        else:
            if query.lower() in "".lower():
                break
            else:
                user_query = query.lower()
                ts = user_query.split(' ')
                excl = ["could", "can", "you", "please", "tell", "me",]
                final_query = ' '.join([t for t in ts if not t in excl])
                print(wikipedia.summary(final_query.lower(), sentences=2))
                say(wikipedia.summary(final_query.lower(), sentences=2))




