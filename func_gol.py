import matplotlib.pyplot as plt
import numpy as np
import time

def make_grid(n): 
    grid = []
    for i in range(n): grid.append([0] * n)
    return grid

def print_grid(grid):
    n = len(grid)

    for i in range(n):
        for j in range(n):
            if grid[i][j] == 0: print(" ", end="")
            else: print("X", end="")
        print(end="\n")

def vis_grid(grid, delay = 0.5):
    plt.clf()
    np_arr = np.array(grid)
    plt.imshow(np_arr, cmap="binary")
    plt.axis("off")
    plt.pause(delay)

def run_vis(grid, steps, delay):
    plt.ion()

    for _ in range(steps): 
        vis_grid(grid, delay)
        grid = update_grid(grid)

    plt.ioff()
    plt.show()


def get_neighbors(i, j):
    dir = [-1, 0, 1]
    cells = []
    
    for a in dir:
        for b in dir:
            if a == 0 and b == 0: continue 
            cells.append((i + a, j + b))
    
    return cells

def get_counts(i, j, grid):
    cells = get_neighbors(i, j)  
    n = len(grid)
    
    alive = 0

    for pair in cells: 
        x, y = pair[0], pair[1]

        if x < 0: x = n - 1
        if x > n - 1: x = 0

        if y < 0: y = n - 1
        if y > n - 1: y = 0

        if grid[x][y] == 1: alive += 1

    # dead = 8 - alive
    return alive

def updated_cell(i, j, grid):
    alive = get_counts(i, j, grid)
    isAlive =(grid[i][j] == 1)

    if isAlive:
        if alive < 2: return 0
        if 2 <= alive <= 3: return 1
        if 3 < alive: return 0
    else:
        if alive == 3: return 1
    return 0

def update_grid(grid):
    n = len(grid)
    next_grid = make_grid(n)

    for i in range(n):
        for j in range(n):
            next_state = updated_cell(i, j, grid)
            next_grid[i][j] = next_state

    return next_grid

def add_glider(i, j, grid):
    grid[i][j] = 1
    grid[i][j + 1] = 1
    grid[i][j + 2] = 1
    grid[i + 1][j + 2] = 1
    grid[i + 2][j + 1] = 1
    return grid

def test_5(): 
    grid = make_grid(100)
    
    grid = add_glider(5, 10, grid)
    grid = add_glider(50, 20, grid)

    run_vis(grid, 256, 0.05)

test_5()   
