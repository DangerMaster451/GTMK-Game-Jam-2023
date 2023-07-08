import pygame
import math
from pygame.math import Vector2

class NPC(pygame.sprite.Sprite):
    def __init__(self, window:pygame.surface.Surface):
        self.window = window
        self.position = Vector2(650, 0)
        self.image = pygame.transform.scale(pygame.image.load("Assets/Images/Sprites/NPC_1.png"), (50,50))
        self.order_image = pygame.transform.scale(pygame.image.load("Assets/Images/Sprites/NPC_1_order.png"), (50,50))
        self.state = "move"
        self.speed = 1
        self.wobble_value = 0
        self.start_order_frame = 0
        self.current_frame = 0

    def update(self):
        match self.state:
            case "move":
                self.move()
            case "start_order":
                self.start_order()
            case "order":
                self.order()
            case "wait":
                self.wait()
            case "leave":
                self.leave()
        self.render()
        self.current_frame += 1

    def move(self):
        self.position.y += self.speed
        self.wobble_value += 1
        if self.position.y > 360:
            self.state = "start_order"
            self.start_order_frame = self.current_frame     

    def start_order(self):
        # play sound effect
        self.wobble_value = 0
        print("starting order...")
        self.state = "order"

    def order(self):          
        if self.current_frame - self.start_order_frame > 60:
            self.state = "wait"

    def wait(self):
        pass
        # TODO idle animation

    def leave(self):
        self.position.y += self.speed
        self.wobble_value += 1
        if self.position.y > 720:
            self.state = "delete"

    def render(self):
        if self.state == "order":
            self.window.blit(self.order_image, self.position)    
        else:
            render_image = pygame.transform.rotate(
                self.image, math.sin(self.wobble_value / 5) * 10
            )
            self.window.blit(render_image, self.position)