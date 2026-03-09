import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # must override
        pass

    def update(self, dt: int):
        # must override
        pass
    
    def colides_with(self, other: "CircleShape") -> bool:
        """
        Check if this object collided with another circular object.
        
        Collision is detected by comparing the distance between the centers
        of the two circles with the sum of their radii.
        
        Args:
            other (CircleShape): The other circular object to check for collision.
        
        Returns:
            bool: True if the circles collide, False otherwise.
        """
        radius_sum = self.radius + other.radius
        if self.position.distance_to(other.position) > radius_sum:
            return False
        return True