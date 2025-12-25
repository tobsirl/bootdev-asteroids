import pygame
import random
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface):
        pygame.draw.circle(
            screen,
            "white",
            (self.position.x, self.position.y),
            self.radius,
            LINE_WIDTH,
        )

    def update(self, dt: float):
        self.position += self.velocity * dt

    def split(self):
        # Remove this asteroid from the game
        self.kill()

        # If already at minimum size, do not spawn smaller ones
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        # Log the split event
        log_event("asteroid_split")

        # Choose a random split angle between 20 and 50 degrees
        angle = random.uniform(20, 50)

        # Create two new velocity vectors by rotating current velocity
        v1 = self.velocity.rotate(angle)
        v2 = self.velocity.rotate(-angle)

        # New radius for the split asteroids
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        # Spawn two smaller asteroids at the same position with boosted speed
        a1 = Asteroid(self.position.x, self.position.y, new_radius)
        a1.velocity = v1 * 1.2

        a2 = Asteroid(self.position.x, self.position.y, new_radius)
        a2.velocity = v2 * 1.2