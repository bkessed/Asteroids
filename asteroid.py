import random
from circleshape import *
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += (self.velocity * dt) 

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        aster = self.velocity.rotate(random_angle)
        smaster = self.velocity.rotate(-random_angle)
        ASTEROID_NEW_RADIUS = self.radius - ASTEROID_MIN_RADIUS
        new_asteroid_1 = Asteroid(self.position.x, self.position.y, ASTEROID_NEW_RADIUS)
        new_asteroid_1.velocity = aster * 1.2
        new_asteroid_2 = Asteroid(self.position.x, self.position.y, ASTEROID_NEW_RADIUS)
        new_asteroid_2.velocity = smaster * 1.2