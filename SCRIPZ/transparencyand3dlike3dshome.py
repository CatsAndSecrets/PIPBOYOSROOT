import pygame
import win32api
import win32con
import win32gui
import time


pygame.init()
screen = pygame.display.set_mode((800, 600), pygame.NOFRAME) # For borderless, use pygame.NOFRAME
done = False
fuchsia = (255, 0, 128)  # Transparency color
dark_red = (139, 0, 0)
coler = (24, 0, 0)
clock = pygame.time.Clock()
image = pygame.image.load("C:\\Users\\tdthe\Pictures\\2021_07_10_the-whole-circusv2-18360095.png").convert_alpha()
# Create layered window
hwnd = pygame.display.get_wm_info()["window"]
win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE,
                       win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)
# Set window transparency color
win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(*fuchsia), 0, win32con.LWA_COLORKEY)
z = 1
angle = 1
angledirection = 1
flip = False
angletr = 1

skippin = 4 #how much of a step to take each new render of the animation. really much, the bigger this is, the chunkier the animation. Nice. its a good thing. i want that.

#todo, add random flickering, or not. ill probably include that as a thing in the main thing over everything

def run():
    global angle, angletr, angledirection, z
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        x, y = pygame.mouse.get_pos()
    for x in range(0, skippin):
        if (angletr+skippin*angledirection) > 90 or (angletr+skippin*angledirection) < 0:
            print("")
            angledirection = angledirection*-1
        angletr += angledirection*skippin
        angle += skippin 
        angle = angle%360
        #angledr = angle%90
        z = (z+1)%100
    print(angletr)
    screen.fill(dark_red)
    #Imaged = pygame.transform.smoothscale(image, (int(((90 - angledr)/90) * image.get_size()[0]),175))
    
    
    if 1 < angle and angle < 90:
        Imaged = pygame.transform.smoothscale(image, (int(((90 - angletr)/90) * 175),175))
        for i in range(round((angletr/10*-1)), round((angletr/10))): 
            screen.blit(pygame.transform.flip(Imaged, False, False), pygame.Rect(100+angletr+i, 100, 175, 175))
            
    elif 90 < angle and angle < 180:
        Imaged = pygame.transform.smoothscale(image, (int(((90 - angletr)/90) * 175),175))
        for i in range(round((angletr/10*-1)), round((angletr/10))): 
            screen.blit(pygame.transform.flip(Imaged, True, False), pygame.Rect(100+angletr-i, 100, 175, 175))
        

    elif 180 < angle and angle < 270:
        Imaged = pygame.transform.smoothscale(image, (int(((90 - angletr)/90) * 175),175))
        for i in range(round((angletr/10*-1)), round((angletr/10))): 
            screen.blit(pygame.transform.flip(Imaged, True, False), pygame.Rect(100+angletr+i, 100, 175, 175))
            
    elif 270 < angle and angle < 360:
        Imaged = pygame.transform.smoothscale(image, (int(((90 - angletr)/90) * 175),175))
        for i in range(round((angletr/10*-1)), round((angletr/10))): 
            screen.blit(pygame.transform.flip(Imaged, False, False), pygame.Rect(100+angletr-i, 100, 175, 175)) 
            

    pygame.display.update()
    
    clock.tick(12)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    run()