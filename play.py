from prep import *

pos = 0,0
maze = get_maze()

while True:
    display(maze, pos)

    choice = input("WASD to move >>> ")
    result = get_new_pos(pos, maze, choice)
    pos = result["position"]
    obj = result["object"]

    if obj == "X":
        display(maze, pos)
        print("you win")
        break
