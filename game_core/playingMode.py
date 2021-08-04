import pygame
from setting import *
from player import Player
from red_ball import Red_ball

import random

class PlayingMode():
    def __init__(self):
        pygame.font.init()
        self.font = pygame.font.Font(pygame.font.match_font("arial", bold=True), 40)
        self.running = True
        self.clock = pygame.time.Clock()
        self.address = "GameMode"
        self.all_ball =pygame.sprite.Group()
        self.player = Player()
        self.wall = Wall()
        self.big_wall = Big_wall()
        self.pinky = Red_ball("pinky",200,400,-2)
        self.punky = Red_ball("punky",500,310,-4)
        self.inky = Red_ball("inky",200,220,-3)
        self.clyde = Red_ball("clyde",500,130,-3)
        self.blinky = Red_ball("blinky",200,40,-4)
        self.edge_up = Edge_up()
        self.edge_down =Edge_down()
        self.edge_left =Edge_left()
        self.edge_right =Edge_right()
        self.transfer＿information = []
        pass

    def update(self,data):    #data為一個dictionary list裡面為字串
        self.all_ball.add(self.pinky,self.punky,self.inky,self.clyde,self.blinky)
        self.all_wall.add(self.wall,self.big_wall,self.edge_up,self.edge_down,self.edge_left,self.edge_right)
        self.transfer＿information = []
        self.player.update(data)
        self.pinky.update()
        self.punky.update()
        self.inky.update()
        self.clyde.update()
        self.blinky.update()
        self.collision()
        self.hit_wall()
        self.transfer＿information.append(self.player.get_ball_data())
        self.transfer＿information.append(self.blinky.ball_info)
        self.transfer＿information.append(self.pinky.ball_info)
        self.transfer＿information.append(self.punky.ball_info)
        self.transfer＿information.append(self.inky.ball_info)
        self.transfer＿information.append(self.clyde.ball_info)
        self.game_over()
        return self.transfer＿information
        pass

    def collision(self):
        hit_red_ball =pygame.sprite.spritecollide(self.player,self.all_ball,False)
        if hit_red_ball:
            self.player.rect.center=[50,25]
            self.player.life -=1
            pass
        pass

    def hit_wall(self):
        if self.player.rect.x <=-30 or self.player.rect.y <= -30:
            self.player.rect.center =[50,25]
        if self.player.rect.x >=530 or self.player.rect.y >= 530:
            self.player.rect.center =[50,25]
        if 70 <= self.player.rect.x <= 142 and -25 <= self.player.rect.y <=420:
            self.player.rect.center =[50,25]
        if 201 <=self.player.rect.x <= 420 and 380 <= self.player.rect.y <=530 :
            self.player.rect.center =[50,25]

    def ticks(self,fps = FPS):
        self.clock.tick(fps)

    def game_over(self):
        if self.player.life == 0:
            self.running = False
            pass

        if self.player.rect.x >= 510 and self.player.rect.y <= -20:
            self.running = False
            pass
        if 425 <= self.player.rect.x <= 530 and -30 <= self.player.rect.y <=30:
            self.running = False
