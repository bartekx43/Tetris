import pygame
import functions

# Constant dimensions of building block
bb_width = 46
bb_height = 46
bb_frame = 3


def building_block(window, x, y, color):
    # Puts together black outline with colored center
    pygame.draw.rect(window, (0, 0, 0), (x, y, bb_width, bb_height))
    pygame.draw.rect(window, color, (x + bb_frame, y + bb_frame, bb_width - 2 * bb_frame, bb_height - 2 * bb_frame))


def build_sprite(window, x, y, color, rotation, build_map):
    building_block(window, x, y, color)
    x_temp, y_temp = x, y
    for letter in build_map:
        if letter == "d":
            y_temp += bb_height - bb_frame
            building_block(window, x_temp, y_temp, color)
        elif letter == "u":
            y_temp -= bb_height - bb_frame
            building_block(window, x_temp, y_temp, color)
        elif letter == "r":
            x_temp += bb_width - bb_frame
            building_block(window, x_temp, y_temp, color)
        elif letter == "l":
            x_temp -= bb_width - bb_frame
            building_block(window, x_temp, y_temp, color)


def L_block(window, x, y, color, rotation):
    build_map = functions.L_dict[rotation]
    build_sprite(window, x, y, color, rotation, build_map)


def K_block(window, x, y, color, rotation):
    build_map = functions.K_dict[rotation]
    build_sprite(window, x, y, color, rotation, build_map)


def S_block(window, x, y, color, rotation):
    build_map = functions.S_dict[rotation]
    build_sprite(window, x, y, color, rotation, build_map)


def O_block(window, x, y, color, rotation):
    build_map = functions.O_dict[rotation]
    build_sprite(window, x, y, color, rotation, build_map)


def Z_block(window, x, y, color, rotation):
    build_map = functions.Z_dict[rotation]
    build_sprite(window, x, y, color, rotation, build_map)


def I_block(window, x, y, color, rotation):
    build_map = functions.I_dict[rotation]
    build_sprite(window, x, y, color, rotation, build_map)
