import pygame

# Constant dimensions of building block
bb_width = 46
bb_height = 46
bb_frame = 3


def building_block(window, x, y, color):
    # Puts together black outline with colored center
    pygame.draw.rect(window, (0, 0, 0), (x, y, bb_width, bb_height))
    pygame.draw.rect(window, color, (x + bb_frame, y + bb_frame, bb_width - 2*bb_frame, bb_height - 2*bb_frame))
