import pygame
from Python.Projects.Games.Tetris import sprites

L_dict = {
    0: "ddr",
    1: "durr",
    2: "rdd",
    3: "rru"
}

L_limits_dict = {
    0: 693,
    1: 736,
    2: 693,
    3: 736
}

K_dict = {
    0: "ddur",
    1: "rdur",
    2: "rudd",
    3: "rudr"
}

K_limits_dict = {
    0: 693,
    1: 736,
    2: 693,
    3: 779
}

Z_dict = {
    0: "rudld",
    1: "rdr",
    2: "rudld",
    3: "rdr"
}

Z_limits_dict = {
    0: 693,
    1: 736,
    2: 693,
    3: 736
}


I_dict = {
    0: "ddd",
    1: "rrr",
    2: "ddd",
    3: "rrr"
}

I_limits_dict = {
    0: 564,
    1: 779,
    2: 564,
    3: 779
}

O_dict = {
    0: "rdl",
    1: "rdl",
    2: "rdl",
    3: "rdl"
}

O_limits_dict = {
    0: 736,
    1: 736,
    2: 736,
    3: 736
}

S_dict = {
    0: "drd",
    1: "rur",
    2: "drd",
    3: "rur"
}

S_limits_dict = {
    0: 693,
    1: 736,
    2: 693,
    3: 736
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


def fall():
    pass

