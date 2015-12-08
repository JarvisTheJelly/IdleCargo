import pygame
import math
import random

GAMESPEED = 5
WIDTH, HEIGHT = 250, 250
SLAY_RADIUS = min(WIDTH, HEIGHT) / 2

def lerp(a, b, t):
    return (1 - t) * a + t * b

class point:

    def __init__(self, initial, height):
        self.initial = initial
        self.pos_base = [WIDTH / 2, HEIGHT / 2 + height]
        self.total = initial
        self.radius = SLAY_RADIUS * math.cos((abs(height) / float(SLAY_RADIUS)) * (math.pi / 2))
        self.color = (lerp(0, 255, abs(height) / SLAY_RADIUS), 30, lerp(0, 255, self.radius / SLAY_RADIUS))

    def update(self, delta):
        self.total += delta
        self.pos = [int(self.pos_base[0] + math.sin(self.total) * self.radius), int(self.pos_base[1])]

    def render(self, surface):
        if math.cos(self.total) > 0:
            surface.set_at(self.pos, self.color)

def main():
    pygame.init()
    screen_size = (WIDTH, HEIGHT)
    screen = pygame.display.set_mode(screen_size)
    
    n = 500
    points = [point(i / math.pi , -SLAY_RADIUS + (float(SLAY_RADIUS) / n) * 2*i) for i in xrange(n)]
    
    clock = pygame.time.Clock()

    done = False
    while not done:
        delta = clock.tick()/1000.0 * GAMESPEED

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    done = True
                if event.key == pygame.K_F2:
                    pygame.image.save(screen, "Icon2.png")

        #screen.fill((0, 0, 0))

        for p in points:
            p.update(delta)
            p.render(screen)

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
