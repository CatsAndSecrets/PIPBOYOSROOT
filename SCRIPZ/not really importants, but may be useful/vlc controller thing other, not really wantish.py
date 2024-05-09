import vlc, time

media_player = vlc.MediaPlayer()
 
media = vlc.Media("What can I do for You.mp4")

media_player.set_media(media)

media_player.play()
#media_player.
time.sleep(10)
print (media_player.get_state(), (media_player.get_state()) == "Playing")
while media_player.get_state() == State.Playing:
    timesleep(.1)