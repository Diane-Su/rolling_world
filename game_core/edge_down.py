import pygame
from setting import *

class Edge_down(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.edge_down_coordinate =(0,598)
        self.edge_down_width =600
        self.edge_down_height =2
        self.edge_down_colcor =BLACK
        self.edge_down_size =pygame.Surface((600,2))
        self.rect =self.edge_down_size.get_rect()
        self.rect.center =(300,599)
        pass