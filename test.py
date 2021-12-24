import pickle
from time import sleep
from prep import *

pos = 0,0
maze = get_maze()
d = pickle.load(open("saved/1.sav", "rb"))

def select_move(possibilities):
    bestmove, bestscore = "w", -1 * 10**10
    for move, score in possibilities.items():
        if score > bestscore:
            bestscore = score
            bestmove = move
    return bestmove

while True:
    display(maze, pos)
    sleep(0.1)

    move = select_move(d[pos])
    result = get_new_pos(pos, maze, move)
    pos = result["position"]
    obj = result["object"]

    if obj == legend["reward"]:
        display(maze, pos)
        print("done!")
        break