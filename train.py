import random
from time import sleep
from prep import *

pos = 0,0
maze = get_maze()

d = {
    (i,j):{"w":0, "a":0, "s":0, "d":0} 
    for i in range(len(maze)) 
    for j in range(len(maze[i]))
}

NUM_ITERATIONS = 100000
SHOW_STEPS = False

for i in range(NUM_ITERATIONS):

    if SHOW_STEPS:
        display(maze, pos)
        sleep(0.01)
    
    else:
        progress = int((i+1)/(NUM_ITERATIONS)*100)
        print(progress*"#"+(100-progress)*"-", i, end="\r")

    move = random.choice("wasd")

    result = get_new_pos(pos, maze, move)
    newpos = result["position"]
    obj = result["object"]

    if obj == legend["reward"]:
        # win the game
        score = d[pos][move]
        d[pos][move] = (score + 10)/2

    elif pos == newpos:
        # never move - probably invalid move
        score = d[pos][move]
        d[pos][move] = (score-1)/2

    elif pos != newpos:
        # moved
        score = d[pos][move]
        d[pos][move] = (score + max(list(d[newpos].values())) * 0.8)/2

    pos = newpos

import os
import pickle 

os.system("mkdir saved")
pickle.dump(d, open("saved/1.sav", "wb"))

for k,v in d.items():
    print(k, v)
