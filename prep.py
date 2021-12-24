from copy import deepcopy

legend = {
    "reward": "X",
    "wall": "#",
    "road": "-",
    "player": "P"
}

def get_maze(filepath="maze.txt"):
    out = []
    with open(filepath) as f:
        for line in f:
            out.append(list(line.strip()))

    return out

def display(maze, pos=(0,0), legend=legend):
    print()
    i,j = pos
    maze = deepcopy(maze)
    maze[i][j] = legend["player"]
    for row in maze:
        print("".join(row))
    print()

def valid_input():
    choice = input("WASD to move >>>").lower()
    while choice not in ["w", "a", "s", "d"]:
        print("Invalid choice")
        choice = input("WASD to move >>>").lower()
    return choice

def get_new_pos(pos, maze, move, legend=legend):
    i,j = pos
    di,dj = {"w":(-1,0), "a": (0,-1), "s":(1,0), "d":(0,1)}[move]
    ni,nj = i+di, j+dj

    if ni<0 or nj<0 or ni>=len(maze) or nj>=len(maze[0]):
        return {"position":pos, "object":"-"}

    new = maze[ni][nj]
    if new == legend["wall"]:
        return {"position":pos, "object":"-"}
    
    return {"position":(ni,nj), "object":new}

