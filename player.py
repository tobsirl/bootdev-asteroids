import pygame
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED
from circleshape import CircleShape   # adjust this import if your project structure is different



class Player(CircleShape):
    def __init__(self, x, y):
        # Call parent constructor with x, y, and radius
        super().__init__(x, y, PLAYER_RADIUS)

        # Player starts with 0 rotation
        self.rotation = 0

    # Provided triangle method (unchanged)
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def rotate(self, dt):
        PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rotation += PLAYER_TURN_SPEED * dt
        if keys[pygame.K_d]:
            self.rotation -= PLAYER_TURN_SPEED * dt

