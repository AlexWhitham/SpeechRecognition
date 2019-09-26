"""
Created on Mon Jul  8 11:57:58 2019

@author: nimir
"""

"""
#Recognition from file
r = sr.Recognizer()
harvard = sr.AudioFile('harvard.wav')
with harvard as source:
  # r.adjust_for_ambient_noise(source)
    audio = r.record(source)
r.recognize_google(audio)
"""

#Install SpeechRecognition, pyaudio, pafy, youtube-dl, python-vlc, gTTS
#Imports
from gtts import gTTS
import os
import pafy as p
import vlc
import speech_recognition as sr
#import time

#Voice function
def fix_text_to_speech(language,mytext,filepath):
    voice = gTTS(text = mytext,lang=language)
    voice.save(filepath)

#Settings
r = sr.Recognizer()
mic = sr.Microphone()
keyword = "Alice"
startcom = ["play","play video", "start"]
pausecom = ["pause", "pause video"]
stopcom = ["stop", "stop video", "end video"]
intro_text = "How can I help?"
intro_path = "C:\\Users\\nimir\\Desktop\\PythonProjects\\start.mp3"
intro_play = "start C:\\Users\\nimir\\Desktop\\PythonProjects\\start.mp3"
error_path = "C:\\Users\\nimir\\Desktop\\PythonProjects\\error.mp3"
error_play = "start C:\\Users\\nimir\\Desktop\\PythonProjects\\error.mp3"
  
#Need to add Listening for the keyword
#r.listen() == keyword

#Get command
with mic as source:
    print(intro_text)
    playvoice = fix_text_to_speech("en",intro_text,intro_path)
    os.system(intro_play)
    audio = r.listen(source,5)

#Try to recognise
try:    
    command = r.recognize_google(audio)
except sr.RequestError:
    print("API unavailable")
    playvoice = fix_text_to_speech("en","API unavailable",error_path)
    os.system(error_play)
    raise sr.RequestError
except sr.UnknownValueError:
    print("Unable to recognise")
    playvoice = fix_text_to_speech("en","Unable to recognise",error_path)
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
    media.pause()  
elif command in stopcom:   
    media.stop()    
elif command not in startcom or pausecom or stopcom:
    playvoice = fix_text_to_speech("en","Command unrecognised",error_path)
    os.system(error_play)    
#state = media.get_state()    
#print(state)   
