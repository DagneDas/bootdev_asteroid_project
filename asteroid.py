import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float):
        self.position = self.position + (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        log_event("asteroid_split")

        moving_angle = random.uniform(20, 50)
        smaller_asteroid_vetor1 = self.velocity.rotate(moving_angle)
        smaller_asteroid_vetor2 = self.velocity.rotate(-moving_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        smaller_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        smaller_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)

        smaller_asteroid1.velocity = smaller_asteroid_vetor1 * 1.2
        smaller_asteroid2.velocity = smaller_asteroid_vetor2 * 1.2
