import random
from prep import *

def is_solvable(maze, start_position=(0,0)):

    seen = set([start_position])
    queue = [start_position]

    while queue:
        i,j = queue.pop(0)
        seen.add((i,j))
        for di,dj in [(1,0),(-1,0),(0,1),(0,-1)]:
            ni,nj = i+di, j+dj

            if (ni,nj) in seen:
                continue

            if ni<0 or nj<0 or ni>=len(maze) or nj>=len(maze[0]):
                continue

            if maze[ni][nj] == "X":
                return True

            if maze[ni][nj] == "#":
                continue

            if maze[ni][nj] == "-":
                seen.add((ni,nj))
                queue.append((ni,nj))

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