"""Main game handler / the engine. Description in the class Doctring."""

import pygame
import DialogueHandler
import AnimationHandler
import World
import random

class Handler(object):
    """The big and most important class. Handles everything.

    This class will handle everything. Entities moving, updating, rendering,
    initialization, and destruction. The game clock, dialogue, game states.
    Basically this class is the game engine.
    """

    def __init__(self):
        """Initializes the game handler.

        Initializes the handler (engine) and all of the variables. Will
        not specifically create entities, as this needs to be as open and
        reusable as possible.
        """
        
        #random.seed(0)

        self.clock = pygame.time.Clock()

        self.entities = []
        self.dialogue_boxes = [] #Dialogue boxes will be qeued up.
        self.to_remove = []

        self.game_state = "GAME"

        self.dialogue_handler = DialogueHandler.DialogueHandler()
        self.animation_handler = AnimationHandler.AnimationHandler()

        self.game_vars = {
                "fps": 60.0,
                "map_w": 256,
                "map_h": 256
                }

        self.world = World.World(self)

    def update(self):
        """Updates the engine and everything in it.

        Loops through and updates every entity, as well as the game clock.

        Returns:
            a boolean value based on if the program is done or not
        """

        #time since the last frame in seconds
        tick = self.clock.tick(self.game_vars["fps"]) / 1000.0

        #Get the Inputs
        pressed_keys = pygame.key.get_pressed()
        pressed_mouse_buttons = pygame.mouse.get_pressed()
        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return True

                if event.key == pygame.K_SPACE:
                    if self.game_state == "DIALOGUE":
                        del self.dialogue_boxes[0]
                        if len(self.dialogue_boxes) == 0:
                            self.game_state = "GAME"

        if self.game_state == "GAME":
            for entity in self.entities:
                self.animation_handler.update(entity, tick)
                entity.update()

            if len(self.dialogue_boxes) > 0:
                self.game_state = "DIALOGUE"

        

        return False

    def render(self, surface):
        """Renders everything

        Renders everyting in the engine to the provided surface. In most
        cases it should be the main python screen.
        """

        #Render the map / world
        surface.fill((0, 0, 0))

        #Render World
        self.world.render(surface, (0, 0))

        #Render Entities
        for entity in self.entities:
            entity.render(surface)

        #Render Dialogue
        if len(self.dialogue_boxes) > 0:
            self.dialogue_handler.render_box(self.dialogue_boxes[0], surface)

    def add_entity(self, entity):
        """appends the entity to the entity list."""

        self.entities.append(entity)

    def remove_entity(self, entity):
        """Adds an entity to the 'to remove' list which is dumped
        every update
        """

        self.to_remove.append(entity)

    def destroy(self):
        """De-initializes all the variables and entities

        Never written someting like this, not sure if it is redundant
        and handled automatically but I figured I would write one anyways.
        """

        del self.entities[:]
        del self #Not sure if this works.
