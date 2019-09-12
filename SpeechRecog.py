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

#Need to install SpeechRecognition, pyaudio, pafy, youtube-dl, python-vlc, gTTS
from gtts import gTTS
import pafy as p
import vlc
#import time

language = "en"
mytext = "Please speak"
voice = gTTS(text = mytext,lang=language)
voice.save("C:\\Users\\nimir\\Desktop\\Python Projects\\start.mp3")
playvoice = vlc.MediaPlayer("C:\\Users\\nimir\\Desktop\\Python Projects\\start.mp3")


import speech_recognition as sr
r = sr.Recognizer()
mic = sr.Microphone()
with mic as source:
    print(mytext) 
    playvoice.play()
    #time.sleep(1.5)
    #duration = playvoice.get_length() / 1000
    #time.sleep(duration)
    audio = r.listen(source)
    
command = r.recognize_google(audio)

if command == "play":
    url = "https://www.youtube.com/watch?v=j2bnj5hMkIw&t=769s"
    video = p.new(url)
    best = video.getbest()
    media = vlc.MediaPlayer(best.url)
    media.play()

#to stop video run this    
media.stop()    