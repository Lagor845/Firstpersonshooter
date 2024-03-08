import math

#Screen
RESOLUTION = WIDTH, HEIGHT = 1600,900
HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2
FPS = 0

#Player
PLAYER_NAME = "Paden"
PLAYER_MAX_HEALTH = 100
PLAYER_POS = 1.5,5
PLAYER_ANGLE = 0
PLAYER_SPEED = 0.004
PLAYER_ROT_SPEED = 0.002

#Camera
FOV = math.pi / 3
HALF_FOV = FOV / 2
NUM_RAYS = WIDTH // 2
HALF_NUM_RAYS = NUM_RAYS // 2
DELTA_ANGLE = FOV / NUM_RAYS
MAX_DEPTH = 20

#Screen Scale
SCREEN_DIST = HALF_WIDTH / math.tan(HALF_FOV)
SCALE = WIDTH // NUM_RAYS

#Networking
SERVER_IP = "192.168.86.218"
PORT = 9999