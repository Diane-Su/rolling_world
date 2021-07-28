from time import process_time
import pygame

from mlgame.view.view import PygameView
from mlgame.gamedev.generic import quit_or_esc
from game_core import rolling_world

FPS = 30
if __name__ == '__main__':
    pygame.init()
    game = rolling_world.Rolling_world()
    scene_init_info_dict = game.get_scene_init_data()
    game_view = PygameView(scene_init_info_dict)
    frame_count = 0
    while game.is_running and not quit_or_esc():
        pygame.time.Clock().tick_busy_loop(FPS)
        commands = game.controller.get_keyboard_command()
        game.update(commands)
        game_progress_data = game.get_scene_progress_data()
        game_view.draw_screen()
        game_view.draw(game_progress_data)
        game_view.flip()
        frame_count += 1

    pygame.quit()