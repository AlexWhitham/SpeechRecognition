"""
Created on Mon Jul  8 11:57:58 2019

@author: nimir
"""

"""
#Testing

#Recognition from file
r = sr.Recognizer()
harvard = sr.AudioFile('harvard.wav')
with harvard as source:
  # r.adjust_for_ambient_noise(source)
    audio = r.record(source)
r.recognize_google(audio)


#state = media.get_state()    
#print(state)

#Get command
with source:
    print(intro_text)
    fix_text_to_speech("en",intro_text,intro_path)
    os.system(intro_play)
    audio = r.listen(source,5)
"""

#Install SpeechRecognition, pyaudio, pafy, youtube-dl, python-vlc, gTTS, swig, pocketsphinx (using pip win)
#Imports
from gtts import gTTS
import os
import pafy as p
import vlc
import speech_recognition as sr
#import time

#Settings
r = sr.Recognizer()
source = sr.Microphone()
#keyword = [("Alice",1),("Hey Alice",1),("Computer",1)]
keyword = "computer"
startcom = ["play","play video", "start"]
pausecom = ["pause", "pause video"]
stopcom = ["stop", "stop video", "end video"]
intro_text = "Hey, how can I help you today?"
intro_path = "C:\\Users\\nimir\\Desktop\\PythonProjects\\start.mp3"
intro_play = "start C:\\Users\\nimir\\Desktop\\PythonProjects\\start.mp3"
error_path = "C:\\Users\\nimir\\Desktop\\PythonProjects\\error.mp3"
error_play = "start C:\\Users\\nimir\\Desktop\\PythonProjects\\error.mp3"

#Voice function
def fix_text_to_speech(language,mytext,filepath):
    voice = gTTS(text = mytext,lang=language)
    voice.save(filepath)

#Listening for the keyword
def activate(my_keyword):
    try:
        with source:
            print("I'm in activate")
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
            transcript = r.recognize_google(audio)
            if transcript.lower() == my_keyword:
                return True
            else:
                return False
    except:
        pass

#Command recognise function
def get_command(audio_input):    
    try:    
        print("I'm in recognise")
        command = r.recognize_google(audio_input)
    except sr.RequestError:
        print("API unavailable")
        fix_text_to_speech("en","API unavailable",error_path)
        os.system(error_play)
        raise sr.RequestError
    except sr.UnknownValueError:
        print("Unable to recognise")
        fix_text_to_speech("en","Unable to recognise",error_path)
        os.system(error_play)
        raise sr.UnknownValueError
    
    #Interpret command into action    
    if command in startcom:
        url = "https://www.youtube.com/watch?v=j2bnj5hMkIw&t=769s"
        video = p.new(url)
        best = video.getbest()
        media = vlc.MediaPlayer(best.url)
        media.play()
    elif command in pausecom:   
        media = vlc.MediaPlayer()
        media.pause()  
    elif command in stopcom:
        media = vlc.MediaPlayer()
        media.stop()    
    elif command not in startcom or pausecom or stopcom:
        fix_text_to_speech("en","Command unrecognised",error_path)
        os.system(error_play)    
  
#Running it in loop        
while True :
    if activate(keyword) == True:
        print("I'm in loop")
        fix_text_to_speech("en",intro_text,intro_path)
        os.system(intro_play)
        with source:
            print(intro_text)
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
            get_command(audio)
                #os.system("OK")
    else:
        pass