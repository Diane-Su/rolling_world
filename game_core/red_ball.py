import pygame
from .setting import *
import sys


class Red_ball(pygame.sprite.Sprite):

    def __init__(self, ball_name, pos_x, pos_y, vel_x):
        pygame.sprite.Sprite.__init__(self)
        self.ball_name = ball_name
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.vel_x = vel_x
        self.direction = ""
        self.ball_info = {}
        self.rect = pygame.Rect(self.pos_x, self.pos_y, 30, 30)
        self.rect.center = self.pos_x, self.pos_y

    def update(self):
        self.ball_info = {"ball_name": self.ball_name,
                          "ball_coordinate": (self.pos_x, self.pos_y),
                          "ball_direction": self.direction
                          }
        self.move()
        return self.ball_info
        pass

    def move(self):
        if self.vel_x < 0:
            self.direction = "Left"
        if self.vel_x > 0:
            self.direction = "Right"
        if self.pos_x > 550 or self.pos_x < 200:
            self.vel_x = -1 * self.vel_x
        self.pos_x += self.vel_x
        self.rect.center = self.pos_x, self.pos_y

    def get_elvesData(self):
        return {"x":self.rect.x,
               "y":self.rect.y,
               "vel":self.vel_x
              }
        pass