import random
from prep import *

def is_solvable(maze, start_pos=(0,0)):

    si,sj = start_pos
    seen = set()
    queue = [(si,sj)]

    while len(queue) > 0:
        # print(len(queue), len(seen))
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

def generate(rows, cols, player_pos=(0,0), reward_pos=None, wall_ratio=0.2):

    dist =  [int(wall_ratio*10), int((1-wall_ratio)*10)]

    if reward_pos==None:
        reward_pos = rows-1, cols-1
    
    out = []
    for i in range(rows):
        row = []
        for j in range(cols):
            obj = random.choices(["#","-"], dist )[0]
            row.append(obj)
        out.append(row)

    out[player_pos[0]][player_pos[1]] = "-"
    out[reward_pos[0]][reward_pos[1]] = "X"

    while not is_solvable(out):
        display(out, (0,0))

        out[random.randrange(rows)][random.randrange(cols)] = "-"
        out[player_pos[0]][player_pos[1]] = "-"
        out[reward_pos[0]][reward_pos[1]] = "X"

    return out


NUM_ROW = 10
NUM_COL = 40
WALL_RATIO = 0.5

maze = generate(NUM_ROW, NUM_COL, wall_ratio=WALL_RATIO)
display(maze, (0,0))

filename = f"{NUM_ROW}x{NUM_COL}.txt"
with open("generated/" + filename, "w") as f:
    for row in maze:
        f.write("".join(row))
        f.write("\n")
    