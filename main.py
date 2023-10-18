import vlc
import time
import os
import RPi.GPIO as GPIO

#setting up gpio
GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BOARD)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)



#setting up the playlist
playlistdir = ("/home/videosynth/Music/songs")
songs = os.listdir(playlistdir)
songplaying = False
songindex = 0
media = vlc.MediaPlayer(playlistdir + "/" + songs[songindex])

while True:
    
    if GPIO.input(10) == GPIO.HIGH and songplaying == False:
        media.play()

    if GPIO.input(10) == GPIO.HIGH and songplaying == True:
        media.stop()
        if songindex < len(songs):
            songindex += 1
        if songindex == len(songs):
            songindex = 0
        
        media = vlc.MediaPlayer(playlistdir + "/" +songs[songindex])


