import speech_recognition as sr#this recognizes the speech as we say in verbally
import webbrowser #this will connect us to browser so any questions asked will be answered 
import pyttsx3#a module to convert text into voice 
import musiclibrary#it helps to use many music using a variable as that variable contains the dictionary of music
import requests # it is used to fetch data from API's and websites
from openai import OpenAI# imports openai API
import os # to import inbuilt operating system
#pip install pocketsphinx

r=sr.Recognizer()#its a class that helps you to take speech recognition functionality 
engine=pyttsx3.init()#  from this our pyttsx will be initialized or starts which let the program talk
def speak(text): 
    engine.say(text)# this is a function that takes any text and make it say by the computer 
    engine.runAndWait()#   computer say it loud


def aiprocess(command):
    

    # Create the client
    client = OpenAI(
        api_key="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"  # Make sure this is a valid key
    )

    # Create a chat completion
    completion = client.chat.completions.create(#This calls the Chat Completions API to generate a response based on a conversation history.
        model="gpt-3.5-turbo",
        # the code below defines the conversation history:  messages is basiclayy choices for duictionaries inside the list if wrtten choices[1] in the print statement 
        #  then it would find the 2nd dictionary under messages as its the choices and if not found kit would give an error but you can create another dictionary as well
        messages=[                  
            {
                "role": "system",
              "content": "You are a helpful virtual assistant named Jarvis skilled in general tasks like Alexa and Google."
              },
            {
                "role": "user",
              "content": command
              }
        ],
    )

    # Print the assistant's reply
    print(completion.choices[1].message.content)#This prints the content of the assistant’s reply. completion.choices[0] 
    # gets the first (and usually only) completion, and .message.content accesses the text of the assistant's reply.

def processcommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")# through this webbrowser you can open links and run them or even a variable which contains a link
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open chat" in c.lower():
        webbrowser.open("https://chatgpt.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song=c.lower().split(" ")[1]# it will actually form a list of ["play","(the song you said)"] and [1] this command is to run the object on the number 1 index(count from 0,1,2,3,4...)
        link=musiclibrary.music[song]# in this i will store the link and then i will play that link in the webbrowser and this takes the music inside music library for pplaying it as musiclibrary takes a dictionary or list of music and in this one the list or dictionry is "music"
        webbrowser.open(link)#Anything you want to search you can in wrbbrowser or open something in webbrowser by the link like this one

    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey=ea6c57b8c39b4f8c83311c28dfa4e8fb")
        # The code below check if the request was successful 
        if r.status_code==200:# 200 means "OK" that means the resoponse has now the data of articles and its succceded i getting the data 
            data = r.json()  # .json basically is a method we got by the request module and it just creates a dictionary of the data in r or anything wrtten in the syntax like this
            articles = data.get('articles', [])#it means get the article from the link and if its empty then get an empty list
            if not articles:
                speak("No new articles found")
                print("No new articles found")
            else:
                for article in articles:
                    speak(article['title'])
                    print(article["title"])
    else:
        #Let OpenAI handle the request
        output=aiprocess(c)
        speak(output)

if __name__=="__main__":# this line means to run this code below direclty and not if it is imported as a module 
    speak("Initializing Jarvis....")
    while True:
    #Listen for the wake word"Jarvis"
    #this obtain audio from the microphone

        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source,timeout=3,phrase_time_limit=2)
                word=r.recognize_google(audio)
            if(word.lower()=="jarvis"):
                speak("Yes,sir")# listens the command that jarvis and the computer will say yes sir
                print("Jarvis Activated")
            #Listen for command
            with sr.Microphone() as source:
                audio = r.listen(source)
            print("recognizing...")
            command=r.recognize_google(audio)
            processcommand(command)
        except Exception as e:
            print("Error; {0}".format(e))







