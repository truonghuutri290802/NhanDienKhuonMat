import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser as wb    
friday = pyttsx3.init()  # khoi tao 
voice = friday.getProperty('voices') #thiet lap giong noi
friday.setProperty('voice',voice[1].id) 

def speak (audio):
    print('F.R.I.D.A.Y : ' + audio)
    friday.say(audio)
    friday.runAndWait()
def time():
    Time = datetime.datetime.now().strftime("%I:%M:%p")
    speak(Time)
def welcome() :
    hour = datetime.datetime.now().hour
    if hour>= 6 and hour <12:
        speak("Good morning sir")
    elif hour >=12 and hour <18:
        speak("Good Afternoon sir")
    elif hour >=18 and hour <24:
        speak("Good night sir")
    speak("How can i help you ?")
def command():
    c =sr.Recognizer()
    with sr.Microphone() as source:
      c.pause_threshold = 2
      audio = c.listen(source)
    try :
        query = c.recognize_google(audio,language='en')
        print("Tris Truong" + query)
    except sr.UnknownValueError:
        print("Please repeat or typing the command")
        query = str(input("Your order is:"))
    return query
if __name__ == "__main__":
    welcome()
    while True:
        query = command().lower() 
        if "google" in query:
            speak("what should iI search boss ?")
            search = command().lower()
            url =f"https://www.google.com.vn/search?q={search}"
            speak(f"Here is your {search} on google")
    