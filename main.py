import pygame
from sys import exit

pygame.init()
resx = 1280
resy = 720
screen = pygame.display.set_mode((resx,resy))
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.fill((94,129,162))
    pygame.display.update()
    clock.tick(60)