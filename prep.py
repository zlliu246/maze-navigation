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