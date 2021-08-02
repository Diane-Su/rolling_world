import pygame
from setting import *
import sys

class Red_ball(pygame.sprite.Sprite):

    def __init__(self,ball_name,pos_x,pos_y,vel_x):
        pygame.sprite.Sprite.__init__(self)
        self.ball_name = ball_name
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.vel_x = vel_x
        self.direction ='None'
        self.ball_info ={}
        self.image_pinky =pygame.image.load(path.join(IMAGE_DIR,"pinky.png"))
        self.image_pinky =pygame.transform.scale(self.image_pinky,(30,30))
        self.rect = self.image_pinky.get_rect()
        self.rect.center =self.pos_x,self.pos_y
        pass

    def update(self):
        self.ball_info = {"ball_name":self.ball_name,
                            "ball_coordinate":self.rect.center,
                          "ball_direction":self.direction
                          }
        self.move()
        return self.ball_info
        pass

    def move(self):
        if self.pos_x > 550 or self.pos_x < 200:
            self.vel_x = -1*self.vel_x
            if self.pos_x > 500:
                self.direction = "left"
            if self.pos_x < 200:
                self.direction = "right"
        self.pos_x += self.vel_x
        self.rect.center = self.pos_x, self.pos_y
        pass
