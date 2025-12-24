from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius=ASTEROID_MIN_RADIUS):
        super().__init__(x, y, radius)