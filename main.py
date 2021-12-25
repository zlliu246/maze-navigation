import random
from prep import *

def is_solvable(maze, start_pos=(0,0)):

    si,sj = start_pos
    seen = set()
    queue = [(si,sj)]

    while len(queue) > 0:
        i,j = queue.pop(0)
        seen.add((i,j))

        for di,dj in [(-1,0),(0,-1),(1,0),(0,1)]:
            ni,nj = i+di, j+dj

            if ni<0 or nj<0 or ni>=len(maze) or nj>=len(maze[0]):
                continue

            obj = maze[ni][nj]

            if obj == "X":
                return True
            
            if obj == "-" and (ni,nj) not in seen:
                queue.append((ni,nj))
                seen.add((ni,nj))

    return False

import os

for filename in os.listdir("solvable"):
    filepath = "solvable/" + filename
    maze = get_maze(filepath)
    print(is_solvable(maze))

print()

for filename in os.listdir("unsolvable"):
    filepath = "unsolvable/" + filename
    maze = get_maze(filepath)
    print(is_solvable(maze))