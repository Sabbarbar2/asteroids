import pygame # type: ignore

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # groups logic
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # overrided by sub-classes
        pass

    def update(self, dt):
        # overrided by sub-classes
        pass
    
    def collision(self, otherCircle):
        distance = self.position.distance_to(otherCircle.position) 
        if distance <= (self.radius + otherCircle.radius):
            return True
        return False
    