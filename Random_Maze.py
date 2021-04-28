# Abedin Sherifi
# RBE 550, Assignment #3
# 02/23/2020
# This function generates a random maze with start position marked as “S”
# on the top left corner and the #goal position marked as “G” at the bottom right corner.
# Obstacles are randomly generated and account #for 30% of the space.
# All of the free spaces are set to spaces ‘ ’

import random

def Random_Maze(n_r, n_c):
    # 2-D Array
    row = n_r
    col = n_c
    maze = [[' ' for i in range(col)] for j in range(row)]
    # Random obstacles added and account for 30% (0.3) of the total space.
    n_obs = round(row * col * .3)
    for i in range(n_obs):
        maze[random.randint(0, row - 1)][random.randint(0, col - 1)] = 'O'
    maze[0][0] = 'S'
    maze[row - 1][col - 1] = 'G'
    return maze

# Input for the generation of the maze (number of rows and number of columns).
if __name__ == '__main__':
    row = 100
    col = 100
    mz = Random_Maze(row, col)
    for row in mz:
        print(' '.join([str(elem) for elem in row]))
