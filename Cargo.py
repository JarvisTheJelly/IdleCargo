#!/usr/bin/env python

"""A simple chill-out cargo game

Not really sure what I plan for this game, but I think I just
want it to be a game where the goal isn't intensity or awesomeness,
but simply to enjoy yourself and have a good time. Current idea,
transporting cargo. Euro Truck Simulator of space.
"""

import pygame
import Handler
import DemoHandler

__author__ = "Nick Jarvis"
__copyright__ = "Nick Jarvis 2015"

__credits__ = ["Nick Jarvis", "Will McGugan"]

__license__ = "GNU General Public License (GPL)"
__version__ = "0.0.1 pre-alpha"
__maintainer__ = "Nick Jarvis"
__email__ = "najarvis2016@gmail.com"
__status__ = "Prototype"

def run():
    pygame.init()
    pygame.font.init()

    screen_size = (640, 480)
    screen = pygame.display.set_mode(screen_size)

    pygame.display.set_caption("Cargo Game")

    game_engine = Handler.Handler()

    main_demo_handler = DemoHandler.DemoHandler(game_engine)
    main_demo_handler.set_up_demo()

    done = False
    while not done:
        done = game_engine.update()

        screen.fill((0, 0, 0))
        game_engine.render(screen)

        pygame.display.flip()
    
    game_engine.destroy()
    pygame.quit()

if __name__ == "__main__":
    run()
