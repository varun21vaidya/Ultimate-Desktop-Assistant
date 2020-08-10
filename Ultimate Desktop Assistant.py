import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib 
import wolframalpha
from random import uniform



engine=pyttsx3.init('sapi5')
voices = engine.getProperty('voices') #pip install pyttsx3==2.6
#print(voices[0].id)  #id is the type of voice male or female, 
engine.setProperty('voice', voices[0].id)  #but our system have only male

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>6 and hour<12:
        speak("Good morning varun") #put here your name
    elif hour>12 and hour<18:
        speak("Good afternoon varun")
    else:
        speak("Good evening varun")
    speak("I am Ultimo, how may I help you")
def sound(s):
    music_dir=r"C:\Users\Admin\Documents\sounds" #create a folder and put sounds for background
    song=os.listdir(music_dir)
    os.startfile(os.path.join(music_dir, song[s]))

def takecommand():
    #takes input from thre user and returns string output
    r=sr.Recognizer() 
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1#takes 1 second pause while listening
        audio=r.listen(source)
        
    try:
        print("Recognizing...")
        sound(0)
        query = r.recognize_google(audio, language='en-in')
        print(f"User Said: {query}\n")
    except Exception as e:
        #print(e)
        
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login("****@gmail.com","**password***") #put here email and password
    server.sendmail("***@gmail.com",to,content) #rewrite your mail
    server.close()
    
        
if __name__=="__main__":
    wishme()
    wake="ultimo"

    while True:
        query=takecommand().lower()
        #logic for tasks
        firefox_path =r"C:\Program Files\Mozilla Firefox\firefox.exe"
        webbrowser.register('firefox',None, webbrowser.BackgroundBrowser(firefox_path))
        #put chrome instead of firefox
        
        if query.count(wake)>0:
            speak("i am ready")
            
    
            if "wikipedia" in query:
                speak ("searching in Wikipedia")
                query=query.replace("wikipedia","")
                query=query.replace("on wikipedia","")
                query=query.replace("ultimo","")
                results=wikipedia.summary(query,sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
                
            elif "youtube" in query:
                query=query.replace("youtube","")
                query=query.replace("on","")
                query=query.replace("ultimo","")
                g="https://www.youtube.com/results?search_query=" + query
            
                speak("playing"+ query)
                webbrowser.get('firefox').open(g)
                
            elif "google" in query:
                
                u="www.google.com"
                webbrowser.get('firefox').open(u)    #opens in firefox
               #webbrowser.open("google.com")    #opens in Internet Explorer
                
            elif "open" in query:
                query=query.replace("open","")
                query=query.replace("ultimo","")
                g="https://www."           
                webbrowser.get('firefox').open(g)    #opens in firefox
               #webbrowser.open(f)    #opens in Internet Explorer
             
            elif "search" in query:
                query=query.replace("search","")
                query=query.replace("ultimo","")
                query=query.replace("on google","")
                g="https://www.google.com/search?q="+query
                speak("searching for"+ query)
                webbrowser.get('firefox').open(g)    #opens in firefox
               #webbrowser.open(f)    #opens in Internet Explorer
           
            elif "play music" in query:
                music_dir=r"E:\songs" #path of your favourite songs
                songs=os.listdir(music_dir)
                #n=int(uniform(1.0,40.0))
                
                os.startfile(os.path.join(music_dir, songs[0]))
                break
            
            elif "word" in query:
                speak("opening word document")
                os.startfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office\Microsoft Office Word 2007.lnk")
                
            elif "excel" in query:
                speak("opening excel document")
                os.startfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office\Microsoft Office Excel 2007.lnk")    
                
           
            elif "the time" in query:
                strtime=datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Sir, the time is {strtime}")
                
           
            elif "start code" in query:
                speak("opening anaconda spyder")
                codepath=r"C:\Users\Admin\anaconda3\pythonw.exe C:\Users\Admin\anaconda3\cwp.py C:\Users\Admin\anaconda3 C:\Users\Admin\anaconda3\pythonw.exe C:\Users\Admin\anaconda3\Scripts\spyder-script.py"
                os.startfile(codepath)
            
            elif "calculate" in query: #register on wolframalpha first
                app_id="YWXX4Q-462JV8VYRR"
                client=wolframalpha.Client(app_id)
                indx=query.split().index('calculate')
                word=query.split()[indx+1:]
                res=client.query(" ".join(word))
                answer=next(res.results).text
                print(answer)
                speak("the answer is"+ answer)
           
            elif "send email" in query:
                try:
                    speak("what should I mail ?")
                    content=takecommand()
                    to="****@gmail.com" #put mail of recipient 
                    sendEmail(to, content)
                    speak("email has been send")
                except Exception as e:
                    print(e)
                    speak("sorry, The email could not be send")
            
            
            elif "quit" in query:
                speak("ok bye")
                sound(1)
                break
                
            
    
    
    