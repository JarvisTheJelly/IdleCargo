"""Main class that handles the game world"""

import pygame
import gametools.VoronoiMapGen as VMG

class World(object):

    def __init__(self, handler):
        self.handler = handler
        self.map_w = handler.game_vars["map_w"]
        self.map_h = handler.game_vars["map_h"]

        self.map_generator = VMG.mapGen()
        
        #self.map_array = self.map_generator.negative(self.map_generator.whole_new_updated((self.map_w, self.map_h), c1=1, c2=-1))
        self.map_array = self.map_generator.negative(self.map_generator.full_updated((self.map_w, self.map_h), rpd=3, ppr=2))

        self.prefab = None

    def render(self, surface, pos):
        if self.prefab is None:
            self.prefab = pygame.Surface((self.map_w, self.map_h))
            dark_surf = pygame.Surface((1, 1))
            for y in xrange(self.map_h):
                for x in xrange(self.map_w):
                    self.prefab.lock()
                    clr = self.map_array[x][y]

                    if clr < 160:
                        self.prefab.set_at((x, y), (0, clr*.1, clr))
                    elif clr < 165:
                        self.prefab.set_at((x, y), (205, 198, 115))
                    elif clr < 190:
                        self.prefab.set_at((x, y), (0, 100, 0))
                    elif clr < 210:
                        self.prefab.set_at((x, y), (50+clr*.1, 50+clr*.1, 50+clr*.1))

                    else:
                        self.prefab.set_at((x, y), (clr, clr, clr))
                    self.prefab.unlock()
                    dark_surf.set_alpha(clr - 127)
                    self.prefab.blit(dark_surf, (x, y))
            
            pygame.image.save(self.prefab, "PrefabSave.png")

        surface.blit(self.prefab, pos)
