import Python.Projects.Games.Tetris.functions
import random

nr = random.randint(1, 2)

if nr == 1:
    from Python.Projects.Games.Tetris.functions import L_dict as Dict
    print(Dict[0])

if nr == 2:
    from Python.Projects.Games.Tetris.functions import K_dict as Dict
    print(Dict[0])
