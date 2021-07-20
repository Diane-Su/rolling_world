import  pygame
from setting import *
class Big_wall(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.big_wall_coordinate =(280,460)
        self.big_wall_width = 320
        self.big_wall_height = 140
        self.big_wall_color = BLACK
        self.big_wall_size =pygame.Surface((320,140))
        self.rect =self.big_wall_size.get_rect()
        self.rect.center =(440,530)
        pass
