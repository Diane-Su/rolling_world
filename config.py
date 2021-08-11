from .game_core.rolling_world import Rolling_world

GAME_VERSION = "1.0"

GAME_PARAMS = {
    "()": {
        "prog": "rolling_world",
        "game_usage": "%(prog)s"
    }
}

GAME_SETUP = {
    "game": Rolling_world,
    "ml_clients": [
        {"name": "1P"}
    ],
}