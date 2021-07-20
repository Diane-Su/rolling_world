import pygame
from setting import *

class Edge_up(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.edge_up_coordinate =(0,0)
        self.edge_up_width =600
        self.edge_up_height =2
        self.edge_up_color =BLACK
        self.edge_up_size =pygame.Surface((600,2))
        self.rect =self.edge_up_size.get_rect()
        self.rect.center =(300,1)
        pass