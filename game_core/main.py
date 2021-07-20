import pygame
from rolling_world import Rolling_world

if __name__ == "__main__":
    pygame.init()
    game = Rolling_world()
    pass
    while game.isRunning():
        game.update()


    pygame.quit()