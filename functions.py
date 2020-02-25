import pygame
from Python.Projects.Games.Tetris import sprites
# import sprites


L_dict = {
    0: "ddr",
    1: "durr",
    2: "rdd",
    3: "rru"
}

L_bot_limits_dict = {
    0: 564,
    1: 607,
    2: 564,
    3: 650
}

L_x_limits_dict = {
    0: (0, 8),
    1: (0, 7),
    2: (0, 8),
    3: (0, 7)
}

K_dict = {
    0: "ddur",
    1: "rdur",
    2: "rudd",
    3: "rudr"
}

K_bot_limits_dict = {
    0: 564,
    1: 607,
    2: 607,
    3: 650
}

K_x_limits_dict = {
    0: (0, 8),
    1: (0, 7),
    2: (0, 8),
    3: (0, 7),
}


Z_dict = {
    0: "duru",
    1: "rdr",
    2: "rudld",
    3: "rdr"
}

Z_bot_limits_dict = {
    0: 607,
    1: 607,
    2: 607,
    3: 607
}

Z_x_limits_dict = {
    0: (0, 8),
    1: (0, 7),
    2: (0, 8),
    3: (0, 7)
}


I_dict = {
    0: "ddd",
    1: "rrr",
    2: "ddd",
    3: "rrr"
}

I_bot_limits_dict = {
    0: 521,
    1: 650,
    2: 521,
    3: 650
}

I_x_limits_dict = {
    0: (0, 9),
    1: (0, 6),
    2: (0, 9),
    3: (0, 6),
}


O_dict = {
    0: "rdl",
    1: "rdl",
    2: "rdl",
    3: "rdl"
}

O_bot_limits_dict = {
    0: 607,
    1: 607,
    2: 607,
    3: 607
}

O_x_limits_dict = {
    0: (0, 8),
    1: (0, 8),
    2: (0, 8),
    3: (0, 8)
}

S_dict = {
    0: "drd",
    1: "rur",
    2: "drd",
    3: "rur"
}

S_bot_limits_dict = {
    0: 564,
    1: 650,
    2: 564,
    3: 650
}

S_x_limits_dict = {
    0: (0, 8),
    1: (0, 7),
    2: (0, 8),
    3: (0, 7)
}


def build_sprite(window, x, y, color, rotation, build_map):
    sprites.building_block(window, x, y, color)
    x_temp, y_temp = x, y
    for letter in build_map:
        if letter == "d":
            y_temp += sprites.bb_height - sprites.bb_frame
            sprites.building_block(window, x_temp, y_temp, color)
        elif letter == "u":
            y_temp -= sprites.bb_height - sprites.bb_frame
            sprites.building_block(window, x_temp, y_temp, color)
        elif letter == "r":
            x_temp += sprites.bb_width - sprites.bb_frame
            sprites.building_block(window, x_temp, y_temp, color)
        elif letter == "l":
            x_temp -= sprites.bb_width - sprites.bb_frame
            sprites.building_block(window, x_temp, y_temp, color)


def random_sprite(window, x, y, color, rotation, number):
    if number == 1:
        sprites.L_block(window, x, y, color, rotation)
    elif number == 2:
        sprites.K_block(window, x, y, color, rotation)
    elif number == 3:
        sprites.S_block(window, x, y, color, rotation)
    elif number == 4:
        sprites.O_block(window, x, y, color, rotation)
    elif number == 5:
        sprites.Z_block(window, x, y, color, rotation)
    elif number == 6:
        sprites.I_block(window, x, y, color, rotation)
