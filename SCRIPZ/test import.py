import pygame
from transparencyand3dlike3dshome import spinnerimageboi

dark_red = (139, 0, 0)
clock = pygame.time.Clock()
screen = pygame.display.set_mode((876, 700), pygame.NOFRAME) # For borderless, use pygame.NOFRAME
done = False
runn = 0
numbr = 1
while not done:
    screen.fill(dark_red)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    spinnerimageboi.run(f"Assets\sprites\ConditionBody0\{numbr}.png", 100, 100, 50, 50)
    numbr = numbr % 8 + 1
    
    pygame.display.update()
    clock.tick(64)