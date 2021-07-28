from playingMode import PlayingMode
from controller import EventController
from gameView import PygameView

class Rolling_world():
    def __init__(self):
        self.gamecore = PlayingMode()
        self.view = PygameView()
        self.controller = EventController()
        self.gameObject = None
        pass

    def get_player_scene_info(self):
        pass

    def update(self, cmds):
        self.gameObject = self.gamecore.update(cmds)
        # self.draw(self.gameObject)
        self.gamecore.ticks()

    def reset(self):

        pass

    def isRunning(self):
        if self.gamecore.running == False:
            self.controller.running = False
        running = self.controller.is_running()
        return running

    def draw(self,object):
        self.view.draw(object)
        self.view.flip()

    def get_scene_info(self):
        """
        Get the scene information
        """
        pass

    def get_game_info(self):
        """
        Get the scene and object information for drawing on the web
        """
        pass

    def get_game_progress(self):
        """
        Get the position of game objects for drawing on the web
        """
        pass

    def get_game_result(self):
        """
        Get the game result for the web
        """
        pass
