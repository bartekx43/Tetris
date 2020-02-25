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


def L_block(window, x, y, color, rotation):
    build_map = functions.L_dict[rotation]
    functions.build_sprite(window, x, y, color, rotation, build_map)


def K_block(window, x, y, color, rotation):
    build_map = functions.K_dict[rotation]
    functions.build_sprite(window, x, y, color, rotation, build_map)


def S_block(window, x, y, color, rotation):
    build_map = functions.S_dict[rotation]
    functions.build_sprite(window, x, y, color, rotation, build_map)


def O_block(window, x, y, color, rotation):
    build_map = functions.O_dict[rotation]
    functions.build_sprite(window, x, y, color, rotation, build_map)


def Z_block(window, x, y, color, rotation):
    build_map = functions.Z_dict[rotation]
    functions.build_sprite(window, x, y, color, rotation, build_map)


def I_block(window, x, y, color, rotation):
    build_map = functions.I_dict[rotation]
    functions.build_sprite(window, x, y, color, rotation, build_map)
