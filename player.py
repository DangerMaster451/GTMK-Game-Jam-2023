import pygame
from pygame.math import Vector2

class Player(pygame.sprite.Sprite):
    def __init__(self, window:pygame.Surface) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.window = window
        self.position = Vector2(self.window.get_size()[0]/2, self.window.get_size()[1]/2)
        self.image = pygame.transform.scale(pygame.image.load("Assets/Tiles/Colored/tile_0004.png"), (50,50)).convert_alpha()
        self.speed = 5

    def update(self) -> None:
        self.move()
        self.render()

    def move(self) -> None:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.position.y -= self.speed
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.position.y += self.speed
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.position.x -= self.speed
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.position.x += self.speed

    def render(self) -> None:
        self.window.blit(self.image, self.position)