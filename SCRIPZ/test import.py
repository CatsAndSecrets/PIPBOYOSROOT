import pygame
#import time

#start = time.time()
dark_red = (139, 0, 0)
from transparencyand3dlike3dshome import spinnerimageboi
clock = pygame.time.Clock()
screen = pygame.display.set_mode((876, 700), pygame.NOFRAME) # For borderless, use pygame.NOFRAME
done = False
runn = 0
img = pygame.image.load("C:\\Users\\tdthe\Pictures\\2021_07_10_the-whole-circusv2-18360095.png").convert_alpha()
numbr = 1
while not done:
    screen.fill(dark_red)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
       # if event.type == pygame.KEYDOWN:
            #if event.key == pygame.K_s:
                #start = time.time()
                #spinnerimageboi.run("C:\\Users\\tdthe\Pictures\\2021_07_10_the-whole-circusv2-18360095.png", 100, 100, 175, 175)
  #  keys=pygame.key.get_pressed()  
   # if keys[pygame.K_s]:
    #print(f"C:\\Users\\tdthe\Downloads\ezgif-1-7bb1fff934-gif-png\\ ({numbr})).png")
    spinnerimageboi.run(f"C:\\Users\\tdthe\Downloads\ezgif-1-7bb1fff934-gif-png\\ ({numbr}).png", 100, 100, 175, 175)
    numbr = numbr % 39 +1
    #if runn == 1:
        #end = 
        #if int(time.time()) - int(start) > 10:
        #    runn = 0
        #else:
            
    print("mario")
    screen.blit(img, pygame.Rect(400, 100, 300, 300))
    pygame.display.update()
    clock.tick(64)