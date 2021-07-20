import pygame
from setting import *

class Edge_left(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.edge_left_coordinate =(0,0)
        self.edge_left_width =2
        self.edge_left_height =600
        self.edge_left_color =BLACK
        self.edge_left_size =pygame.Surface((2,600))
        self.rect =self.edge_left_size.get_rect()
        self.rect.center=(1,300)
        pass
