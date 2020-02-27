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


def set_array(x_cord, y_cord, color, color_array, movement_string, y_limit_array):
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


def y_approx(y, y_grid_cords):
    i = 0

    if y < 5:
        return y_grid_cords[i]

    while i < len(y_grid_cords) and y >= y_grid_cords[i]:
        i += 1
    return y_grid_cords[i-1]


def block_in_array(x, y, coord_array):
    for row in coord_array:
        for column in row:
            if column == (x, y):
                return True
    return False


def is_ok(x, y, build_map, coord_array, x_grid_cords, y_grid_cords):

    y_approximated_higher = y_approx(y, y_grid_cords)
    y_approximated_lower = y_approximated_higher + 43
    x_temp, y_temp = x, y

    if block_in_array(x_temp, y_approximated_higher, coord_array) or block_in_array(x_temp, y_approximated_lower, coord_array) or y_temp >= 650:
        return False

    if x_temp > x_grid_cords[9] or x_temp < 0:
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

        if x_temp > x_grid_cords[9] or x < 0:
            return False

        y_approximated_higher = y_approx(y_temp, y_grid_cords)
        y_approximated_lower = y_approximated_higher + 43
        if block_in_array(x_temp, y_approximated_higher, coord_array) or block_in_array(x_temp, y_approximated_lower, coord_array) or y_temp >= 650:
            return False

    return True


def is_ok_x(x, y, build_map, coord_array, x_grid_cords, y_grid_cords):

    if x < 5:
        return False
    if x > 392:
        return False

    x_index = x_grid_cords.index(x)
    y_index = y_grid_cords.index(y)

    if coord_array[x_index][y_index] != (0, 0):
        return False

    for letter in build_map:
        if letter == "d":
            y_index += 1
        elif letter == "u":
            y_index -= 1
        elif letter == "r":
            x_index += 1
        elif letter == "l":
            x_index -= 1

        if x_index < 0:
            return False

        if x_index > 9:
            return False

        if coord_array[x_index][y_index] != (0, 0):
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


def coordinate_array(coord_array, color_array, x_grid_cords, y_grid_cords):
    for i, row in enumerate(color_array):
        for j, column in enumerate(row):
            if column == (0, 0, 0):
                coord_array[i][j] = (0, 0)
            else:
                coord_array[i][j] = (x_grid_cords[i], y_grid_cords[j])


def row_full(row):
    for color in row:
        if color == (0, 0, 0):
            return False
    return True


def one_down(color_array, row_index):
    i = row_index
    while i > 0:
        for j, color in enumerate(color_array[i]):
            color_array[i][j] = color_array[i-1][j]
        i -= 1

    for index in range(len(color_array[0])):
        color_array[0][index] = (0, 0, 0)


def delete_full_rows(color_array):

    transpose = [[color_array[j][i] for j in range(len(color_array))] for i in range(len(color_array[0]))]

    for i, row in enumerate(transpose):
        if row_full(row):
            one_down(transpose, i)
            color_array = [[transpose[j][i] for j in range(len(transpose))] for i in range(len(transpose[0]))]
            color_array = delete_full_rows(color_array)
    return color_array
