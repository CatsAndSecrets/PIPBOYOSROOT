import pygame
import win32api
import win32con
import win32gui
import time
#also has imag espinning for 3ds ish thing. ITS WORKING!!!

pygame.init()
screen = pygame.display.set_mode((800, 600), pygame.NOFRAME) # For borderless, use pygame.NOFRAME
done = False
fuchsia = (255, 0, 128)  # Transparency color
dark_red = (139, 0, 0)
coler = (24, 0, 0)
clock = pygame.time.Clock()
image = pygame.image.load("C:/Users/tdthe/Pictures/pixil-frame-0 (8) (1).png").convert_alpha()
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
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        x, y = pygame.mouse.get_pos()
    if angle == 90 or angle == 0:
        angledirection = angledirection * -1
    angle += angledirection
    screen.fill(dark_red)  # Transparent background
    pygame.draw.rect(screen, coler, pygame.Rect(100, 100, 175, 175))
    #angle 
    z = (z+1)%100
    print(angle)
    Imaged = pygame.transform.smoothscale(image, (int(((90 - angle)/90) * image.get_size()[0]),175))
    if flip == False: #flip doenst do much yet tho
        for i in range(round((angle/10*-1)), round((angle/10))):
            screen.blit(Imaged, pygame.Rect(100+angle+i, 100, 175, 175))
    else:
        for i in range(round((angle/10*-1)), round((angle/10))):
            screen.blit(pygame.transform.flip(Imaged, False, True), pygame.Rect(100+angle+i, 100, 175, 175))
    pygame.display.update()
    
    clock.tick(32)