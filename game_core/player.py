import pygame   #player
from setting import *

class Player(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.life = 2
        self.ball_info = {}
        self.directions = ""
        self.image =pygame.Surface((20,40))
        self.image =pygame.image.load(path.join(IMAGE_DIR,"pacman.png"))
        self.rect =self.image.get_rect()
        pass

    def update(self,command):
        self.ball_move(command)
        return self.rect.center
        pass

    def ball_move(self,direction):
        if "MOVE_UP" in direction["Data"]:   #往上移動
            self.rect.y -=5
            self.directions = "up"
        if "MOVE_DOWN" in direction["Data"]:  #往下移動
            self.rect.y +=5
            self.directions = "down"
        if "MOVE_RIGHT" in direction["Data"]:   #往右移動
            self.rect.x +=4
            self.directions = "right"
        if "MOVE_LEFT" in direction["Data"]:   #往左移動
            self.rect.x -=4
            self.directions = "left"

            pass

    def get_ball_data(self):   #要傳資料給gameView 包含座標、和球的名稱
        self.ball_info = {"ball_name":"Blue_ball",
                            "ball_coordinate":self.rect.center,
                           "ball_direction":self.directions
                           }
        return self.ball_info