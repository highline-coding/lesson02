import pygame
from random import randint

pygame.init()
screen = pygame.display.set_mode((500, 500))
done = False
is_blue = True
x = 30
y = 30

clock = pygame.time.Clock()
if is_blue: 
    color = (0, 128, 255)
else: 
    color = (255, 100, 0)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                is_blue = not is_blue

    
    
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]: 
        y -= 3
    if pressed[pygame.K_DOWN]: 
        y += 3
    if pressed[pygame.K_LEFT]: 
        x -= 3
    if pressed[pygame.K_RIGHT]: 
        x += 3
    if pressed[pygame.K_SPACE]:
        color = (randint(0,255), randint(0,255), randint(0,255))
    if pressed[pygame.K_t]:
        x += randint(-50, 50)
        y += randint(-50, 50)
    if pressed[pygame.K_c]:
        x = 150
        y = 150

    
    screen.fill((0, 0, 0))
    
    pygame.draw.rect(screen, color, pygame.Rect(x, y, 60, 60))
    
    pygame.display.flip()
    clock.tick(60)
