import pygame
from setting import *
class Edge_right(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.edge_right_coordinate =(598,0)
        self.edge_right_width =2
        self.edge_right_height =600
        self.edge_right_color =BLACK
        self.edge_right_size =pygame.Surface((2,600))
        self.rect =self.edge_right_size.get_rect()
        self.rect.center =(599,1)
        pass