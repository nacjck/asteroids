from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, ASTEROID_SPLIT_VELOCITY_FACTOR
import pygame
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            split_angle = random.uniform(20, 50)
            split_radius = self.radius - ASTEROID_MIN_RADIUS
            self._create_smaller_asteroids(split_angle, split_radius, ASTEROID_SPLIT_VELOCITY_FACTOR)

    def _create_smaller_asteroids(self, split_angle, new_radius, velocity_factor):
            ast1 = Asteroid(self.position.x, self.position.y, new_radius)
            ast1.velocity = self.velocity.rotate(split_angle) * velocity_factor
            ast2 = Asteroid(self.position.x, self.position.y, new_radius)
            ast2.velocity = self.velocity.rotate(-split_angle) * velocity_factor
            
