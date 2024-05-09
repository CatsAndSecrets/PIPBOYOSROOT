import pygame
import sys
import vlc
import time

#Goal - pygame overlay, //pause menu raeally.          has pause, and closing video.      see if can add rewind/ forward.

pygame.init()

WindowW = 480
WindowH = 270

Window = pygame.display.set_mode((WindowW, WindowH))

Instance = vlc.Instance("--no-xlib")
MediaPlayer = vlc.MediaPlayer()
Media = vlc.Media("GIVE ME YOUR TEETH!!! - 1080.mp4")
MediaPlayer.set_media(Media)
    
WinID = pygame.display.get_wm_info()['window']

if sys.platform == "linux2":
    MediaPlayer.set_xwindow(WinID)
elif sys.platform == "win32":
    MediaPlayer.set_hwnd(WinID)
elif sys.platform == "darwin":
    MediaPlayer.set_agl(WinID)

# Scale Down Video Stream
MediaPlayer.video_set_scale(0.2)

#MediaPlayer.play()
MediaPlayer.video_set_mouse_input(False)
MediaPlayer.video_set_key_input(False)

Running = True
playing = "False"
pause = False
#isplaying = True
print("is playsz", MediaPlayer.is_playing())
if MediaPlayer.is_playing():
    print("haea")

while Running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False
        if event.type == pygame.MOUSEBUTTONUP and playing == "False":
            MediaPlayer.play()
            playing = "start"
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                MediaPlayer.pause()
                if pause == True:
                    pause = False
                else:
                    pause = True
                time.sleep(.1)
            if event.key == pygame.K_x:
                playing = "False"
                print("is'nt")
                MediaPlayer.stop()
                pause = False

            #if event.key == pygame.K_RIGHT:
                #location += 1

    if MediaPlayer.is_playing() == 1 and playing == "start":
        playing = "True"
        print("beguned")
    elif MediaPlayer.is_playing() == 0 and playing == "True" and pause == False:
        playing = "False"
        print("is'nt")
        MediaPlayer.stop()


    #if not MediaPlayer.is_playing() = 1:
        #print("ending")
        #
        #playing = False
        #print("ended")
    #print(MediaPlayer.is_playing)
    # Random Red Rectangle (Covered up when video is active)
    
    Window.fill((0, 100, 10))
    pygame.draw.rect(Window, (255, 0, 0), (20, 40, 30, 50))
    pygame.display.flip()

MediaPlayer.stop()
pygame.quit()