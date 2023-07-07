import pygame
import math
from pygame.math import Vector2

class Player(pygame.sprite.Sprite):
    def __init__(self, window:pygame.Surface) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.window = window
        self.position = Vector2(self.window.get_size()[0]/2, self.window.get_size()[1]/2)
        self.image = pygame.transform.scale(pygame.image.load("Assets/Custom/Player.png"), (50,50))
        self.speed = 5
        self.wobble_value = 0

    def update(self) -> None:
        self.move()
        self.render()

    def move(self) -> None:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.position.y -= self.speed
            self.wobble_value += 1
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.position.y += self.speed
            self.wobble_value += 1
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.position.x -= self.speed
            self.wobble_value += 1
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.position.x += self.speed
            self.wobble_value += 1

    def render(self) -> None:
        render_image = pygame.transform.rotate(self.image, math.sin(self.wobble_value/5) * 10)
        self.window.blit(render_image, self.position)