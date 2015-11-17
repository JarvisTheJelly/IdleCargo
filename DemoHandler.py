"""Creates stuff in the world to keep other files clean"""

import pygame
import Entity
import gametools.ImageLoader as ImageLoader
import DialogueHandler
import AnimationHandler


class DemoHandler(object):
    """Class for creating and running the demo.

    Instead of manually calling and creating the entities in one of
    the other files, I want to keep those as open as possible. This
    will allow the game to be set up in a separate file and keep those
    clean.
    """

    def __init__(self, engine):
        """just initializes the demo handler, doesn't set up anything."""

        self.engine = engine
        self.image_loader = ImageLoader.ImageLoader()
        self.dialogue_handler = DialogueHandler.DialogueHandler()
        self.animation_handler = AnimationHandler.AnimationHandler()

    def set_up_demo(self):
        """Here is where the actual demo will be set up.

        Scripting a specific level can all go in here, but in the future
        I want levels to be created in separate files (xml, txt, etc),
        then loaded in to this function.
        """

        player_animation = self.animation_handler.load_animation("CargoSpriteSheet", 16, 16, 0, 0, 3)
        player_entity = Entity.Entity(self.engine, (200, 150), player_animation[0])
        player_entity.add_animation("Idle", player_animation)
        player_entity.selected_animation = "Idle"
        self.engine.add_entity(player_entity)

        metal_animation = self.animation_handler.load_animation("CargoSpriteSheet", 16, 16, 3, 0, 5)
        metal_entity = Entity.Entity(self.engine, (300, 300), metal_animation[0])
        metal_entity.add_animation("default", metal_animation)
        metal_entity.selected_animation = "default"
        self.engine.add_entity(metal_entity)
