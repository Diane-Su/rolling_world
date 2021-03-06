import pygame  # player
from .setting import *


class Player(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.life = 2
        self.ball_info = {}
        self.directions = ""
        self.rect = pygame.Rect(50, 0, 50, 50)
        pass

    def update(self, command):
        self.ball_move(command)
        return self.rect.center

    def ball_move(self, direction):
        if "MOVE_UP" in direction["1P"]:  # 往上移動
            self.rect.y -= 5
            self.directions = "Up"
        if "MOVE_DOWN" in direction["1P"]:  # 往下移動
            self.rect.y += 5
            self.directions = "Down"
        if "MOVE_RIGHT" in direction["1P"]:  # 往右移動
            self.rect.x += 4
            self.directions = "Right"
        if "MOVE_LEFT" in direction["1P"]:  # 往左移動

            self.rect.x -= 4
            self.directions = "Left"

            pass

    def get_ball_data(self):  # 要傳資料給gameView 包含座標、和球的名稱
        self.ball_info = {"ball_name": "Blue_ball",
                          "ball_coordinate": (self.rect.x, self.rect.y),
                          "ball_direction": self.directions
                          }
        return self.ball_info
