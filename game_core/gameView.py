import os

from setting import *
from os import path
import pygame

img_dir =path.join(path.dirname(__file__),'image')

class PygameView():

    def __init__(self):
        pygame.display.init()
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        pygame.display.set_caption("Rolling World")
        self.address = "GameView"
        # self.screen.blit(lives, (490,540))

    def draw(self,data):
        # {"red_ball":red_ball,}
        self.screen.fill((0, 0, 0))
        pygame.draw.rect(self.screen, (2,3,232),[150, 0, 10, 450], 4)
        pygame.draw.rect(self.screen, (2,3,232),[0, 0, 2, 600], 0)
        pygame.draw.rect(self.screen, (2,3,232),[598, 0, 2, 600], 0)
        pygame.draw.rect(self.screen, (2,3,232),[0, 0, 600, 2], 0)
        pygame.draw.rect(self.screen, (2,3,232),[0, 598, 600, 2], 0)
        pygame.draw.rect(self.screen, (2,3,232),[280, 460, 320, 140], 4)
        player = pygame.image.load(path.join(img_dir,"pacman.png")).convert()
        player = pygame.transform.scale(player, (50, 50))
        pinky =pygame.image.load(path.join(img_dir,"pinky.png")).convert()
        pinky =pygame.transform.scale(pinky,(30,30))
        # print("Data in gameview : {}".format(data))
        # pygame.transform.flip(Surface, true, false)
        # pygame.transform.rotate(Surface, angle)

        for dic in data:
            if dic["ball_name"] == "Blue_ball":
                if dic["ball_direction"] == "":
                    self.screen.blit(pygame.transform.flip(player, True, False), dic["ball_coordinate"])
                if dic["ball_direction"] == "left":
                    self.screen.blit(pygame.transform.flip(player, False, False), dic["ball_coordinate"])
                if dic["ball_direction"] == "right":
                    self.screen.blit(pygame.transform.flip(player, True, False), dic["ball_coordinate"])
                if dic["ball_direction"] == "down":
                    self.screen.blit(pygame.transform.flip(pygame.transform.rotate(player, 90), True, False), dic["ball_coordinate"])
                if dic["ball_direction"] == "up":
                    self.screen.blit(pygame.transform.flip(pygame.transform.rotate(player, -90), True, False), dic["ball_coordinate"])

                # pygame.draw.circle(self.screen, (0,0,255), dic["ball_coordinate"], 20, 0)
            #else:
                #if dic["ball_direction"] == "left":
                    #self.screen.blit(pygame.transform.flip(enemy, False, False), dic["ball_coordinate"])
                #if dic["ball_direction"] == "right":
                    #self.screen.blit(pygame.transform.flip(enemy, True, False), dic["ball_coordinate"])
        self.screen.blit(self.screen, (0,0))

    def draw_screen(self):
        self.screen.fill((0, 0, 0))

    def flip(self):
        pygame.display.flip()