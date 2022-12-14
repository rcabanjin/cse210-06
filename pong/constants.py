import pathlib
from game.casting.color import Color

# -------------------------------------------------------------------------------------------------- 
# GENERAL GAME CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# GAME
GAME_NAME = "Batter"
FRAME_RATE = 60

# SCREEN
SCREEN_WIDTH = 1040
SCREEN_HEIGHT = 680
CENTER_X = SCREEN_WIDTH / 2
CENTER_Y = SCREEN_HEIGHT / 2

# FIELD
FIELD_TOP = 60
FIELD_BOTTOM = SCREEN_HEIGHT
FIELD_LEFT = 0
FIELD_RIGHT = SCREEN_WIDTH

# FONT
FONT_FILE = "pong/assets/fonts/zorque.otf"
FONT_SMALL = 32
FONT_LARGE = 48

# SOUND
BOUNCE_SOUND = "pong/assets/sounds/boing.wav"
WELCOME_SOUND = "pong/assets/sounds/start.wav"
OVER_SOUND = "pong/assets/sounds/over.wav"

# TEXT
ALIGN_CENTER = 0
ALIGN_LEFT = 1
ALIGN_RIGHT = 2

# COLORS
BLACK = Color(0, 0, 0)
WHITE = Color(255, 255, 255)
PURPLE = Color(255, 0, 255)

# KEYS
LEFT_1 = "a"
RIGHT_1 = "d"
LEFT_2 = "j"
RIGHT_2 = "l"
SPACE = "space"
ENTER = "enter"
PAUSE = "p"

# SCENES
NEW_GAME = 0
TRY_AGAIN = 1
NEXT_LEVEL = 2
IN_PLAY = 3
GAME_OVER = 4

# LEVELS
LEVEL_FILE = "pong/assets/data/level-{:03}.txt"
BASE_LEVELS = 5

# -------------------------------------------------------------------------------------------------- 
# SCRIPTING CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# PHASES
INITIALIZE = 0
LOAD = 1
INPUT = 2
UPDATE = 3
OUTPUT = 4
UNLOAD = 5
RELEASE = 6

# -------------------------------------------------------------------------------------------------- 
# CASTING CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# STATS
STATS_GROUP = "stats"
DEFAULT_LIVES = 5
MAXIMUM_LIVES = 5

# HUD
HUD_MARGIN = 15
LIVES_GROUP_1 = "lives1"
LIVES_GROUP_2 = "lives2"
SCORE_GROUP = "score"
LEVEL_FORMAT = "LEVEL: {}"
LIVES_FORMAT_1 = "LIVES-1: {}"
LIVES_FORMAT_2 = "LIVES-2: {}"
SCORE_FORMAT = "SCORE: {}"

# BALL
BALL_GROUP = "balls"
BALL_IMAGE = "pong/assets/images/000.png"
BALL_WIDTH = 28
BALL_HEIGHT = 28
BALL_VELOCITY = 7

# RACKET1
RACKET_GROUP_1 = "rackets1"
RACKET_IMAGES_1 = [f"pong/assets/images/{n:03}.png" for n in range(100, 103)]
RACKET_WIDTH_1 = 106
RACKET_HEIGHT_1 = 50
RACKET_RATE_1 = 6
RACKET_VELOCITY_1 = 7

# RACKET2
RACKET_GROUP_2 = "rackets2"
RACKET_IMAGES_2 = [f"pong/assets/images/{n:03}.png" for n in range(103, 105)]
RACKET_WIDTH_2 = 106
RACKET_HEIGHT_2 = 600
RACKET_RATE_2 = 6
RACKET_VELOCITY_2 = 7

# BRICK
BRICK_GROUP = "bricks"

""""
BRICK_IMAGES = {
    "b": [f"pong/assets/images/{i:03}.png" for i in range(10,19)],
    "g": [f"pong/assets/images/{i:03}.png" for i in range(20,29)],
    "p": [f"pong/assets/images/{i:03}.png" for i in range(30,39)],
    "y": [f"pong/assets/images/{i:03}.png" for i in range(40,49)]
}

BRICK_WIDTH = 80
BRICK_HEIGHT = 28
BRICK_DELAY = 0.5
BRICK_RATE = 4
BRICK_POINTS = 50
"""

# DIALOG
DIALOG_GROUP = "dialogs"
ENTER_TO_START = "PRESS ENTER TO START"
PREP_TO_LAUNCH = "PREPARING TO LAUNCH"
WAS_GOOD_GAME = "GAME OVER"