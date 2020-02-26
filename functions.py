import pygame
#from Python.Projects.Games.Tetris import sprites
import sprites
from functools import partial


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


def set_array (x_cord, y_cord, color, color_array, movement_string, y_limit_array):
    for letter in movement_string:
        if letter == "r":
            x_cord += 1
            color_array[x_cord][y_cord] = color
        if letter == "l":
            x_cord -= 1
            color_array[x_cord][y_cord] = color
        if letter == "u":
            y_cord -= 1
            color_array[x_cord][y_cord] = color
        if letter == "d":
            y_cord += 1
            color_array[x_cord][y_cord] = color

# def ground_sprite(window, x, y, color, rotation, build_map, array, x_grid_cords, y_grid_cords):
#
#    array_x = x_grid_cords.index(x)


def is_ok(x, y, build_map, y_limit_array, x_grid_cords): # Problem here, just doenst trigger for some
    x_temp, y_temp = x, y
    if y_limit_array[x_grid_cords.index(x)] <= y:
        return False

    for letter in build_map:
        if letter == "d":
            y_temp += sprites.bb_height - sprites.bb_frame
        elif letter == "u":
            y_temp -= sprites.bb_height - sprites.bb_frame
        elif letter == "r":
            x_temp += sprites.bb_width - sprites.bb_frame
        elif letter == "l":
            x_temp -= sprites.bb_width - sprites.bb_frame

        if y_limit_array[x_grid_cords.index(x)] <= y_temp:
            print(x_temp, y_temp)
            return False

    return True


def update_array(x, y, build_map, y_limit_array, x_grid_cords):
    x_temp, y_temp = x, y
    index = x_grid_cords.index(x)
    y_limit_array[index] = y - 43
    for letter in build_map:
        if letter == "d":
            y_temp += 43
        elif letter == "u":
            y_temp -= 43
            if y_temp <= y_limit_array[x_grid_cords.index(x_temp)]:
                y_limit_array[x_grid_cords.index(x_temp)] = y_temp - 43
        elif letter == "r":
            x_temp += sprites.bb_width - sprites.bb_frame
            if y_temp <= y_limit_array[x_grid_cords.index(x_temp)]:
                y_limit_array[x_grid_cords.index(x_temp)] = y_temp - 43
        elif letter == "l":
            x_temp -= sprites.bb_width - sprites.bb_frame
            if y_temp <= y_limit_array[x_grid_cords.index(x_temp)]:
                y_limit_array[x_grid_cords.index(x_temp)] = y_temp - 43
