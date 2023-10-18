import vlc
import time

def audio(source):
    vlc_instance = vlc.Instance()

    player = vlc_instance.media_player_new()

    media = vlc_instance.media_new(source)

    player.set_media(media)

    player.play()

    time.sleep(0.5)

    duration = player.get_length()

    print("Duration : " + str(duration))

audio("~/Music/sleepyhead.mp3")


