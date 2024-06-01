import pygame
import win32api
import win32con
import win32gui
import time
import math

##no longer transparent. purely for spinning. i do not hav any idea why i decided for them to be together in the first place. probbably lazyness honestly

screen = pygame.display.set_mode((876, 700), pygame.NOFRAME) # For borderless, use pygame.NOFRAME
pygame.init()

done = False
fuchsia = (255, 0, 128)  # Transparency color
dark_red = (139, 0, 0)
coler = (24, 0, 0)
clock = pygame.time.Clock()
#image = pygame.image.load("C:\\Users\\tdthe\Pictures\\2021_07_10_the-whole-circusv2-18360095.png").convert_alpha() # make use local imkage to the project
# Create layered window


#hwnd = pygame.display.get_wm_info()["window"]
#win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE,
#                       win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)
# Set window transparency color
#win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(*fuchsia), 0, win32con.LWA_COLORKEY)

angle = 1
angledirection = 1
angletr = 1

skippin = 1 #how much of a step to take each new render of the animation. really much, the bigger this is, the chunkier the animation. Nice. its a good thing. i want that.

#todo, add random flickering, or not. ill probably include that as a thing in the main thing over everything
class spinnerimageboi():
    def run(imagelocation, xs, ys, width, height):
        global angle, angletr, angledirection
        image = pygame.image.load(imagelocation).convert_alpha()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                x, y = pygame.mouse.get_pos()
        for x in range(0, skippin):
            if (angletr+skippin*angledirection) > 90 or (angletr+skippin*angledirection) < 0:
                #print("")
                angledirection = angledirection*-1
        angletr += angledirection*skippin
        angle += skippin 
        angle = angle%360
      
        #print(angletr)
    
    
        if 1 < angle and angle < 90:
            Imaged = pygame.transform.smoothscale(image, (int(((90 - angletr)/90) * width),height))
            for i in range(round((angletr/10*-1)), round((angletr/10)+1)): 
                
                
                screen.blit(pygame.transform.flip(Imaged, False, False), pygame.Rect(xs+angletr+i, ys, width, height))
            
        elif 90 < angle and angle < 180:
            Imaged = pygame.transform.smoothscale(image, (int(((90 - angletr)/90) * width),height))
            for i in range(round((angletr/10*-1)), round((angletr/10)+1)): 
                
                
                screen.blit(pygame.transform.flip(Imaged, True, False), pygame.Rect(xs+angletr-i, ys, width, height))
        

        elif 180 < angle and angle < 270:
            Imaged = pygame.transform.smoothscale(image, (int(((90 - angletr)/90) * width),height))
            for i in range(round((angletr/10*-1)), round((angletr/10)+1)): 
                
                
                screen.blit(pygame.transform.flip(Imaged, True, False), pygame.Rect(xs+angletr+i, ys, width, height))
            
        elif 270 < angle and angle < 360:
            Imaged = pygame.transform.smoothscale(image, (int(((90 - angletr)/90) * width),height))
            for i in range(round((angletr/10*-1)), round((angletr/10)+1)): 
                
                screen.blit(pygame.transform.flip(Imaged, False, False), pygame.Rect(xs+angletr-i, ys, width, height))
        elif angle == 1:
            Imaged = pygame.transform.smoothscale(image, (int(((90 - angletr)/90) * width),height))
            screen.blit(pygame.transform.flip(Imaged, False, False), pygame.Rect(xs+angletr, ys, width, height))

        #pygame.display.update()
    
        #clock.tick(12)
    
    #while not done:
     #   for event in pygame.event.get():
      #      if event.type == pygame.QUIT:
       #         done = True
    #run()