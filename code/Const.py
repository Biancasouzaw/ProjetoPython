# C
import pygame

C_BLACK= (0, 0, 0)
C_BLUE = (0, 0, 255)
C_GREY = (215, 215, 215)
C_WHITE =(255, 255, 255)
C_PURPLE =(128, 0, 128)
C_RED = (255, 0, 0)

# E
EVENT_ENEMY = pygame.USEREVENT + 1
ENTITY_SPEED = {
    'Level1Bg0': 2,
    'Level1Bg1': 0,
    'Player1': 3,
    'Player2': 3,
    'Enemy1': 3, #3,
    'Enemy2': 4, #2,
    'Energy': 5,  #3,
}


ENTITY_HEALTH = {
    'Level1Bg0': 999,
    'Level1Bg1': 999,
    'Player1': 300,
    'Player2': 300,
    'Enemy1': 1,#50,
    'Enemy2': 1,#60,
    'Energy': 1,
}

ENTITY_DAMAGE = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Player1': 1,
    'Player2':1,
    'Enemy1':60,#1,
    'Enemy2':60,#1,
    'Energy':0,
}

ENTITY_SCORE = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Player1': 0,
    'Player2': 0,
    'Enemy1': 0,  # 1,
    'Enemy2': 0,  # 1,
    'Energy': 15,
}

# M
MENU_OPTION = ('NEW GAME 1P',
               'NEW GAME 2P - COOPERATIVE',
               'NEW GAME 2P - COMPETITIVE',
               'SCORE',
               'EXIT')

# P
PLAYER_KEY_UP = {'Player1': pygame.K_UP,
                 'Player2': pygame.K_w}
PLAYER_KEY_DOWN = {'Player1': pygame.K_DOWN,
                 'Player2': pygame.K_s}
PLAYER_KEY_LEFT = {'Player1': pygame.K_LEFT,
                 'Player2': pygame.K_a}
PLAYER_KEY_RIGHT = {'Player1': pygame.K_RIGHT,
                 'Player2': pygame.K_d}
#PLAYER_KEY_SHOOT = {'Player1': pygame.K_RCTRL,
#               'Player2': pygame.K_LCTRL}

# S
SPAWN_TIME = 4000

# W
WIN_WIDTH = 576
WIN_HEIGHT = 324