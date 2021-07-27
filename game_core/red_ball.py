import pygame
from setting import *
import sys

class Red_ball(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.pinky_pos_x = 200
        self.pinky_pos_y = 400
        self.pinky_vel_x = -3
        self.direction ='None'
        self.ball_info ={}
        self.image_pinky =pygame.image.load(path.join(IMAGE_DIR,"pinky.png"))
        self.rect = self.image_pinky.get_rect()
        self.rect.center =self.pinky_pos_x,self.pinky_pos_y
        pass

    def update(self):
        self.ball_info = {"ball_name":"red_ball",
                            "ball_coordinate":self.rect.center,
                          "ball_direction":self.direction
                          }
        self.move()
        return self.ball_info
        pass

    def move(self):
        if self.pinky_pos_x > 550 or self.pinky_pos_x < 200:
            self.pinky_vel_x = -1*self.pinky_vel_x
            if self.pinky_pos_x > 500:
                self.direction = "left"
            if self.pinky_pos_x < 200:
                self.direction = "right"
        self.pinky_pos_x += self.pinky_vel_x
        self.rect.center = self.pinky_pos_x, self.pinky_pos_y
        pass
