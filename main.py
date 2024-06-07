import pygame, sys, os, pickle, pygame.freetype, time
from pygame._sdl2 import Window
from startup.py import deitrix
pygame.freetype.init()
#from SCRIPZ.header import Header

os.chdir('Assets/')

pygame.init
scrx, scry = 876, 700    # was screen_width and screen_height
screen = pygame.display.set_mode((scrx, scry), pygame.NOFRAME,)
pygame.mouse.set_visible(False)
clock = pygame.time.Clock()
running = True


backColr = ( 0, 4, 0)
#mainColr = pygame.image.load(os.path.join('./ConditionBody0/1.png'))     #(20, 200, 20)
#mainColr = pygame.transform.scale_by(mainColr, 1)
colr = (168, 113, 50)
secolr = (0, 20, 0)
maintab = 1
headerxzs = 1    #change when have the dial to be whicherver th edial is pointing to

class rad(pygame.sprite.Sprite):
    def __init__(self, width, height):
        super().__init__()
        self.images = []         #color.convert_alpha()
        self.index = 0
        for num in range(1, 32):
            img = pygame.image.load(f'sprites/bodycond0frames/{num}.png')
            self.images.append(img)
            self.images.append(img)
            self.images.append(img)
        
        self.image = self.images[self.index]
        
        #self.image.fill(colr, special_flags=pygame.BLEND_RGBA_MIN)
       
        self.rect = self.image.get_rect()
        self.image.fill((255, 255, 255, 0), special_flags=pygame.BLEND_RGBA_MAX)
        self.image.fill(colr, special_flags=pygame.BLEND_RGBA_MIN)
        self.rect.center = (5*(scrx/12), 5*(scry/12))
        #pygame.image.load(os.path.join('./1.png'))


    def update(self):

        self.index = self.index+1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]
        self.image.fill((255, 255, 255, 0), special_flags=pygame.BLEND_RGBA_MAX)
        self.image.fill(colr, special_flags=pygame.BLEND_RGBA_MIN)
        
        #self.rect.center = (5*(scrx/12), 5*(scry/12))
        self.rect.x = 5*(scrx/12)
        self.rect.y = 5*(scry/12)


def GeneralGUI():
    global headerxzs
    zfontzs = pygame.freetype.Font(f'fonts/4_$Terminal_Font_Share-TechMono.ttf', 30)
    #zfontzs.render_to(screen, (170, 5), ('STATS'), (colr))  
    zfontzs.render_to(screen, (280, 5), ('ITEMS'), (colr))  
    zfontzs.render_to(screen, (398, 5), ('DATA'), (colr))   # difference of 23 between
    #zfontzs.render_to(screen, (500, 5), ('MAP'), (colr))   
    zfontzs.render_to(screen, (578, 5), ('RADIO'), (colr))  
    
    pygame.draw.rect(screen, colr, (20, 30, 3, 10))
    pygame.draw.rect(screen, colr, (scrx-23, 30, 3, 10))
    if headerxzs == 1:
        a, b = 142, 253
    if headerxzs == 2:
        a, b = 252, 363
    if headerxzs == 3:
        a, b = 366, 470
    if headerxzs == 4:
        a, b = 472, 551
    if headerxzs == 5:
        a, b = 550, 665

    pygame.draw.rect(screen, colr, (20, 30, a, 3))
    pygame.draw.rect(screen, colr, (b, 30, 856-b, 3))

    pygame.draw.rect(screen, colr, (20+a-3, 15, 3, 15))
    pygame.draw.rect(screen, colr, (20+a, 15, 5, 3))

    pygame.draw.rect(screen, colr, (b, 15, 3, 15))
    pygame.draw.rect(screen, colr, (b-5, 15, 5, 3))
    


    #pygame.draw.rect(screen, colr, (20, 30, 418 - prlkts, 3))
    #pygame.draw.rect(screen, colr, (418 + prlkts, 30, 418 -prlkts + 20, 3))


    
    pygame.draw.rect(screen, secolr, (40, 40,200, 30))



deitrix.Bootstrap(colr, backColr, time)     #make nirmal when want startup




stats_group = pygame.sprite.Group()
items_group = pygame.sprite.Group()
data_group = pygame.sprite.Group()
map_group = pygame.sprite.Group()
radio_group = pygame.sprite.Group()

rads = rad(20, 15)
#headd = Header()
stats_group.add(rads)




while running:
       #when have the rotary encoder, use that

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHTBRACKET:
                if headerxzs < 5:
                    headerxzs += 1
            if event.key == pygame.K_LEFTBRACKET:
                if headerxzs > 1:
                    headerxzs -= 1
    screen.fill(backColr)

    # RENDER YOUR GAME HERE
    
    pos = pygame.mouse.get_pos()
 
    
    #colr = (0, (pos[0] % 255), 100, 255)
    #secolr = (  0,   (pos[1] % 255),   0)
    #rads.image.fill(colr, special_flags=pygame.BLEND_RGBA_MIN)
    pygame.draw.rect(screen, (255, 100, 5, 20), (200, 300,200, 100))
    pygame.draw.rect(screen, (5, 100, 255, 20), (250, 350,200, 100))

    stats_group.draw(screen)
    GeneralGUI()

    if headerxzs == 1:
        stats_group.update()
        

    # flip() the display to put your work on screen
    pygame.display.update()
    
    clock.tick(32)  # limits FPS to 60

pygame.quit()