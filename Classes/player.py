import pygame
import math
from pygame.math import Vector2


class Player(pygame.sprite.Sprite):
    def __init__(self, window: pygame.Surface) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.window = window
        self.position = Vector2(
            self.window.get_size()[0] / 2, self.window.get_size()[1] / 2
        )
        self.image = pygame.transform.scale(
            pygame.image.load("Assets/Images/Sprites/Player.png"), (50, 50)
        )
        self.speed = 7
        self.wobble_value = 0
        self.limit_position = Vector2(135, 135)
        self.limit_size = Vector2(405, 405)
        self.item = None
        self.item_texture = None

    def update(self) -> None:
        self.move()
        self.render()

    def check_for_collisions(self) -> bool:
        if (
            self.position.x < self.limit_position.x
            or self.position.x > self.limit_size.x + self.limit_position.x
        ):
            return True
        elif (
            self.position.y < self.limit_position.y
            or self.position.y > self.limit_size.y + self.limit_position.y
        ):
            return True
        else:
            return False

    def move(self) -> None:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and not keys[pygame.K_a] and not keys[pygame.K_d]:  # up
            self.position.y -= self.speed
            if self.check_for_collisions():
                self.position.y += self.speed
            self.wobble_value += 1
        elif keys[pygame.K_s] and not keys[pygame.K_a] and not keys[pygame.K_d]:  # down
            self.position.y += self.speed
            if self.check_for_collisions():
                self.position.y -= self.speed
            self.wobble_value += 1
        elif keys[pygame.K_a] and not keys[pygame.K_w] and not keys[pygame.K_s]:  # left
            self.position.x -= self.speed
            if self.check_for_collisions():
                self.position.x += self.speed
            self.wobble_value += 1
        elif (
            keys[pygame.K_d] and not keys[pygame.K_w] and not keys[pygame.K_s]
        ):  # right
            self.position.x += self.speed
            if self.check_for_collisions():
                self.position.x -= self.speed
            self.wobble_value += 1

        elif keys[pygame.K_w] and keys[pygame.K_a] and not keys[pygame.K_d]:  # up left
            self.position.x -= self.speed / 2
            self.position.y -= self.speed / 2
            if self.check_for_collisions():
                self.position.x += self.speed / 2
                self.position.y += self.speed / 2
            self.wobble_value += 1
        elif keys[pygame.K_w] and keys[pygame.K_d] and not keys[pygame.K_a]:  # up right
            self.position.x += self.speed / 2
            self.position.y -= self.speed / 2
            if self.check_for_collisions():
                self.position.x -= self.speed / 2
                self.position.y += self.speed / 2
            self.wobble_value += 1
        elif (
            keys[pygame.K_s] and keys[pygame.K_a] and not keys[pygame.K_d]
        ):  # down left
            self.position.x -= self.speed / 2
            self.position.y += self.speed / 2
            if self.check_for_collisions():
                self.position.x += self.speed / 2
                self.position.y -= self.speed / 2
            self.wobble_value += 1
        elif (
            keys[pygame.K_s] and keys[pygame.K_d] and not keys[pygame.K_a]
        ):  # down right
            self.position.x += self.speed / 2
            self.position.y += self.speed / 2
            if self.check_for_collisions():
                self.position.x -= self.speed / 2
                self.position.y -= self.speed / 2
            self.wobble_value += 1


    def is_moving(self) -> bool:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] or keys[pygame.K_s] or keys[pygame.K_a] or keys[pygame.K_d]:
            return True
        else:
            return False

    def render(self) -> None:
        if self.is_moving() == False:
            self.wobble_value = 0
        render_image = pygame.transform.rotate(
            self.image, math.sin(self.wobble_value / 5) * 10
        )
        self.window.blit(render_image, self.position)