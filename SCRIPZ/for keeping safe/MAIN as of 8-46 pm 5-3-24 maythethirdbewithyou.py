import pygame, sys, os

os.chdir('C:/users/tdthe/downloads/PIP BOY OS ROOT/Assets/sprites/')

backColr = (  0,   0,   0)
#mainColr = pygame.image.load(os.path.join('./ConditionBody0/1.png'))     #(20, 200, 20)
#mainColr = pygame.transform.scale_by(mainColr, 1)
colr = (0, 200, 100)

class rad(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        #self.image = color.convert_alpha
        
        #coloredSurface = color.copy()
        #color_surface(coloredSurface, 120, 78, 240)
        #image = image.copy()
        #image.fill((0, 0, 0, 255), None, pygame.BLEND_RGBA_MULT)
        #image.fill(newColor[0:3] + (0,), None, pygame.BLEND_RGBA_ADD)

        
        self.image = color.convert_alpha()
        self.image.fill(colr, special_flags=pygame.BLEND_RGBA_MIN)
        #self.image.
        # this works on images with per pixel alpha too

        ##self.image = self.image.fill((255, 255, 255), mainColr, special_flags=pygame.BLEND_RGBA_MIN)

        self.rect = self.image.get_rect()
        

    def update(self, x):
        self.image.fill((255, 255, 255, 0), special_flags=pygame.BLEND_RGBA_MAX)
        self.image.fill(colr, special_flags=pygame.BLEND_RGBA_MIN)
        print(x)



pygame.init
screen_width, screen_height = 876, 700
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
running = True

block_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()

rads = rad(pygame.image.load(os.path.join('./ConditionBody0/1.png')), 20, 15)
all_sprites_list.add(rads)




while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(backColr)

    # RENDER YOUR GAME HERE
    
    pos = pygame.mouse.get_pos()
 
    rads.rect.x = 5*(screen_width/12)
    rads.rect.y = 5*(screen_height/12)
    colr = (0, (pos[0] % 255), 100, 255)
    #rads.image.fill(colr, special_flags=pygame.BLEND_RGBA_MIN)

    all_sprites_list.draw(screen)
    all_sprites_list.update(4)
    # flip() the display to put your work on screen
    pygame.display.update()

    clock.tick(60)  # limits FPS to 60

pygame.quit()