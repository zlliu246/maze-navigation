from prep import *

pos = 0,0
maze = get_maze()

while True:
    display(maze, pos)

    choice = valid_input()
    result = get_new_pos(pos, maze, choice)
    pos = result["position"]
