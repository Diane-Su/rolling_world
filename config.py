from .game_core.rolling_world import Rolling_world

from os import path
from mlgame.utils.parse_config import read_json_file, parse_config

config_file = path.join(path.dirname(__file__), "game_config.json")
config_data = read_json_file(config_file)
GAME_PARAMS = parse_config(config_data)
GAME_VERSION = config_data["version"]

# GAME_VERSION = "1.0"
#
# GAME_PARAMS = {
#     "()": {
#         "prog": "rolling_world",
#         "game_usage": "%(prog)s"
#     }
# }

GAME_SETUP = {
    "game": Rolling_world,
    "ml_clients": [
        {"name": "1P"}
    ],
}