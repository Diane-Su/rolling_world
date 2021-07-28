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

    def get_scene_init_data(self):
        # TODO
        pass

    def get_scene_prgress_data(self):
        # TODO
        pass

    def game_to_player_data(self):
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

    def get_game_result(self):
        """
        Get the game result for the web
        """
        pass
