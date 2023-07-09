import pygame
from pygame import Vector2
import math, random


class Particle:
    def __init__(
        self,
        window: pygame.surface.Surface,
        position: Vector2,
        velocity: Vector2,
        image: pygame.surface.Surface,
        scale: Vector2,
        life: int,
    ) -> None:
        self.window = window
        self.position = position
        self.velocity = velocity
        self.image = image
        self.scale = scale
        self.life = life

    def update(self):
        self.move()
        self.render()
        self.life -= 1

    def move(self):
        self.position += self.velocity

    def render(self):
        render_image = pygame.transform.scale(
            self.image,
            (self.scale.x * (self.life / 1000), self.scale.y * (self.life / 1000)),
        )
        self.window.blit(render_image, self.position)


def spawn_particles(
    window: pygame.surface.Surface,
    particles: list[Particle],
    position: Vector2,
    image: pygame.surface.Surface,
    scale: Vector2,
    life: int,
) -> list[Particle]:
    
    total_particles = random.randint(0, 1)
    for _ in range(total_particles):
        direction = math.radians(random.randint(0, 359))
        velocity = Vector2(math.sin(direction), math.cos(direction)) * (
            random.random() + 1
        )

        particles.append(Particle(window, position, velocity, image, scale, life))

    return particles
