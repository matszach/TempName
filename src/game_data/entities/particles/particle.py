from src.game_data.entities.entity import Entity
from src.controllers.entity_handlers import PLAYER


# parent class to all pickups
class Particle(Entity):

    # ===== lifecycle =====
    def passive_work(self):

        # animate every frame
        self.animate()

        # expire on end of duration
        self.duration_left -= 1
        if self.duration_left < 0:
            self.expire()

    # constructor
    def __init__(self, sprite_set, travel_direction, display_size=0.3, collision_size=0.2, animation_timer=10,
                 velocity=0.1, duration=60):

        # super constructor
        Entity.__init__(self, sprite_set, display_size, collision_size, animation_timer)

        # direction of particles's travel, overrides Entity's "dir" as they serve the same purpose here
        self.dir = travel_direction

        # distance in units that the projectile travels every frame
        self.v = velocity

        # duration left before the particle expires
        self.duration_left = duration
