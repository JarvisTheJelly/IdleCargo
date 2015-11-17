"""Class that describes a single entity. More detail in the docstring
of the class.
"""

from gametools.vector2 import Vector2 as vec2


class Entity(object):
    """Class for a single Entity.

    An entity is a single object that updates, renders, can be created
    or destroyed. A player, enemy, building, bullet, etc. are all excamples
    of entities. Second most important class (behind the engine).
    """

    def __init__(self, world, pos, image):
        """Initializes the entity.

        Arguments:
            world - the main game engine / handler.
            pos - the initial starting position of the entity.
            image - the image of the entity

        TODO: Create a system for efficiently creating entities
        """

        self.world = world
        self.pos = vec2(pos[0], pos[1])
        self.vel = vec2(0, 0)

        self.base_image = image #I use base image in case animation is added.
        self.image = self.base_image
        self.image_rect = self.base_image.get_rect()
        
        self.animations = {}
        self.selected_animation = None
        self.ani_timer = 0.0
        self.ani_frame = 0

        self.update() #Call update once to set the position of the rect.

    def add_animation(self, ani_name, animation):
        """Adds an existing animation to the Entity"""
        self.animations[ani_name] = animation

    def update(self):
        """updates the entity."""

        self.pos += self.vel
        
        if self.selected_animation is not None:
            self.image = self.animations[self.selected_animation][self.ani_frame]
            self.image_rect = self.image.get_rect()
        self.image_rect.center = self.pos

    def render(self, surface):
        """Renders the entity to the surface at its position"""

        surface.blit(self.image, self.image_rect)
