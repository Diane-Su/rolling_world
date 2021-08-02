import pygame
from setting import *
from player import Player
from wall import Wall
from big_wall import Big_wall
from red_ball import Red_ball
from edge_up import Edge_up
from edge_down import Edge_down
from edge_left import Edge_left
from edge_right import Edge_right

import random

class PlayingMode():
    def __init__(self):
        pygame.font.init()
        self.font = pygame.font.Font(pygame.font.match_font("arial", bold=True), 40)
        self.running = True
        self.clock = pygame.time.Clock()
        self.address = "GameMode"
        self.all_ball =pygame.sprite.Group()
        self.all_wall =pygame.sprite.Group()
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
            self.player.rect.center=[75,50]
            self.player.life -=1
            pass
        pass

    #def hit_wall(self):
        #if self.player.rect.x <=0 and self.player.rect.y <= 0:
            #self.player.rect.center =[75,50]
        #if self.player.rect.x >=600 and self.player.rect.y >= 600:
            #self.player.rect.center =[75,50]

    def ticks(self,fps = FPS):
        self.clock.tick(fps)

    def game_over(self):
        if self.player.life == 0:
            #self.running = Falsec
            pass

        if self.player.rect.x >= 570 and self.player.rect.y <= 30:
            #self.running = False
            pass
