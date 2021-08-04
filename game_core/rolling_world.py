from os import path
import pygame
from setting import *
from playingMode import PlayingMode
from controller import EventController
# from gameView import PygameView
from mlgame.gamedev.game_interface import PaiaGame
from mlgame.view.test_decorator import check_game_progress
from mlgame.view.view_model import create_rect_view_data, create_text_view_data, create_asset_init_data, create_image_view_data, Scene

class Rolling_world(PaiaGame):
    def __init__(self):
        super().__init__()
        self.scene = Scene(width=600, height=600, color="#000000", bias_x=0, bias_y=0)
        self.gamecore = PlayingMode()
        self.controller = EventController()
        self.gameObject = None
        self.is_running = True
        pass

    def get_scene_init_data(self):
        pacman = create_asset_init_data("pacmanLeft", 54, 51, path.join(IMAGE_DIR,"pacmanLeft.png") , "url")
        pacmanR = create_asset_init_data("pacmanRight", 54, 51, path.join(IMAGE_DIR,"pacmanRight.png") , "url")
        pacmanU = create_asset_init_data("pacmanUp", 54, 51, path.join(IMAGE_DIR,"pacmanUp.png") , "url")
        pacmanD = create_asset_init_data("pacmanDown", 54, 51, path.join(IMAGE_DIR,"pacmanDown.png") , "url")
        pinky = create_asset_init_data("pinkyLeft", 50, 50, path.join(IMAGE_DIR,"pinkyLeft.png"), "url")
        pinkyR = create_asset_init_data("pinkyRight", 50, 50, path.join(IMAGE_DIR,"pinkyRight.png"), "url")
        punky = create_asset_init_data("punkyLeft", 50, 50, path.join(IMAGE_DIR,"punkyLeft.png"), "url")
        punkyR = create_asset_init_data("punkyRight", 50, 50, path.join(IMAGE_DIR,"punkyRight.png"), "url")
        clyde = create_asset_init_data("clydeLeft", 50, 50, path.join(IMAGE_DIR,"clydeLeft.png"), "url")
        clydeR = create_asset_init_data("clydeRight", 50, 50, path.join(IMAGE_DIR,"clydeRight.png"), "url")
        inky = create_asset_init_data("inkyLeft", 50, 50, path.join(IMAGE_DIR,"inkyLeft.png"), "url")
        inkyR = create_asset_init_data("inkyRight", 50, 50, path.join(IMAGE_DIR,"inkyRight.png"), "url")
        blinky = create_asset_init_data("blinkyLeft", 50, 50, path.join(IMAGE_DIR,"blinkyLeft.png"), "url")
        blinkyR = create_asset_init_data("blinkyRight", 50, 50, path.join(IMAGE_DIR,"blinkyRight.png"), "url")
        fruit = create_asset_init_data("fruit", 50, 52, path.join(IMAGE_DIR,"fruit.png"), "url" )
        scene_init_data = {"scene": self.scene.__dict__,
                           "assets": [pacman, pinky, punky, clyde, inky, blinky,
                           pacmanR, pinkyR, punkyR,clydeR, inkyR, blinkyR,pacmanU,pacmanD, fruit]
                           }
        return scene_init_data

    def get_scene_progress_data(self):
        listOfObject = []
        playerDirection = "Right"
        enemyDirection = "Right"
        listOfObject.append(create_image_view_data("fruit", 555, 20, 25, 26, 0))
        listOfObject.append(create_rect_view_data("center_wall", 150, 0, 10, 450, "0202e8", 0))
        listOfObject.append(create_rect_view_data("corner_wall", 280, 460, 320, 10, "0202e8", 0))
        listOfObject.append(create_rect_view_data("corner_wall", 280, 460, 10, 140, "0202e8", 0))
        for dic in self.gameObject:
            if dic["ball_name"] == "Blue_ball":
                if dic["ball_direction"]!="":
                    playerDirection = dic["ball_direction"]
                if dic["ball_direction"] == "Up" or dic["ball_direction"] == "Down":
                    listOfObject.append(create_image_view_data("pacman"+playerDirection, dic["ball_coordinate"][0],dic["ball_coordinate"][1], 51, 54, 0))
                else:
                    listOfObject.append(create_image_view_data("pacman"+playerDirection, dic["ball_coordinate"][0],dic["ball_coordinate"][1], 54, 51, 0))
            else:
                if dic["ball_direction"]!="":
                    enemyDirection = dic["ball_direction"]
                listOfObject.append(create_image_view_data(dic["ball_name"]+enemyDirection, dic["ball_coordinate"][0],dic["ball_coordinate"][1], 54, 51, 0))
        game_progress = {
            "background": [],
            "object_list": listOfObject,
            "toggle": [],
            "foreground": [],
            "user_info": [],
            "game_sys_info": {}
        }
        return game_progress

    def game_to_player_data(self):
        pass

    def update(self, cmds):
        self.gameObject = self.gamecore.update(cmds)
        self.gamecore.ticks()

    def reset(self):

        pass

    def isRunning(self):
        if self.gamecore.running == False:
            self.controller.running = False
        self.is_running = self.controller.is_running()
        return self.is_running

    # def draw(self,object):
    #     self.view.draw(object)
    #     self.view.flip()

    def get_game_result(self):
        """
        Get the game result for the web
        """
        pass


    def get_keyboard_command(self):
        cmd_1p = ["None"]
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            cmd_1p.append("MOVE_LEFT")
        if keys[pygame.K_RIGHT]:
            cmd_1p.append("MOVE_RIGHT")
        if keys[pygame.K_UP]:
            cmd_1p.append("MOVE_UP")
        if keys[pygame.K_DOWN]:
            cmd_1p.append("MOVE_DOWN")

        return {"1P": cmd_1p}
