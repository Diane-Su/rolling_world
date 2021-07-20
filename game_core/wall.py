import pygame   #wall
from setting import *

class Wall(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.rectangle_position_coordinate =(150,0)
        self.rectangle_height = 450
        self.rectangle_width = 10
        self.rectangle_color = BLACK
        self.wall_size =pygame.Surface((10,450))
        self.rect =self.wall_size.get_rect()
        self.rect.center =(155,225)
        pass

