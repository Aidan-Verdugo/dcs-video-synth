import vlc
import time
import os

playlistdir = ("/home/videosynth/Music/songs")


songs = os.lsitdir(playlistdir)

runner = 1

while runner != 0:
    media = vlc.MediaPlayer(playlistdir + "/" + songs[1])
    media.play()
    time.sleep(15)


