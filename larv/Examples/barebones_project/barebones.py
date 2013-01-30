import pygame
import sys
from pygame.locals import *
from __ColorConstants import *

import larv
from EntityFactory import EntityFactory
from RenderSystem import RenderSystem

### GLOBALS
FPS = 60

WIN_WIDTH = 800
WIN_HEIGHT = 680
### /GLOBALS


def main():
    global FPSCLOCK, DISPLAYSURF
    pygame.init()
    # Create clock to manage frames
    FPSCLOCK = pygame.time.Clock()
    # Create main surface
    DISPLAYSURF = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

    while True:
        runGame()

def runGame():
    # Initialize the framework
    entity_factory = EntityFactory()
    engine = larv.Engine(entity_factory)

    # Create entities
    entity_factory.createHero()

    # Create systems
    render_system = RenderSystem(DISPLAYSURF)

    # Add systems to the engine
    engine.addSystem(render_system, 0) # priority, less is before

    game_over = False
    while not game_over:
        DISPLAYSURF.fill(WHITE)

        # Handle events
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()

        # Update the game (engine updates every single system in priority order)
        engine.update()
        # Update the window (paint everything)
        pygame.display.update()
        # Wait so FPS get accomplished
        FPSCLOCK.tick(FPS)

def terminate():
    """Ends the game and closes everything."""
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()