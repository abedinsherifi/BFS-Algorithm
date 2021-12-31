# Abedin Sherifi

import time
import os
import matplotlib.pyplot as plt

class Grid():
    def __init__(self, str):
        self.maze = str.splitlines()

    def g_s(self):
        x_r = next(i for i, line in enumerate(self.maze) if "S" in line)
        y_c = self.maze[x_r].index("S")
        return x_r, y_c

    # This function solves the specified maze using BFS Algorithm. The usual BFS psuedo code is
    # followed.
    def main(self, row, col):
        queue = []
        visited = {}
        visited[(row, col)] = (-1, -1)
        queue.append((row, col))

        while len(queue) > 0:
            row, col = queue.pop(0)
            if self.maze[row][col] == 'G':
                path = []
                while row != -1:
                    path.append((row, col))
                    row, col = visited[(row, col)]
                path.reverse()
                return path

            for dr, dc in ((-1, 0), (0, -1), (1, 0), (0, 1)):
                new_r = row + dc
                new_c = col + dr
                if (0 <= new_r < len(self.maze) and
                        0 <= new_c < len(self.maze[0]) and
                        not (new_r, new_c) in visited and
                        self.maze[new_r][new_c] != 'O'):
                    visited[(new_r, new_c)] = (row, col)
                    queue.append((new_r, new_c))
        return

# Open the .txt file that contains the specific maze and read the maze in the file.
loc = "/home/dino/Documents/"
for file in os.listdir(loc):
    if file.startswith("graph500_500") and file.endswith(".txt"):
            fx = open(file)
            file_contents = fx.read()
            print(file_contents)

maze = Grid(file_contents)

start_time = time.time()
path = maze.main(*maze.g_s())
num_of_moves = len(path)
end_time = time.time()
solve_time = end_time - start_time

# Print number of moves and solve time for the specified maze.
if len(path) > 0:
    print(path)
    print("Solution Found in {} seconds".format(solve_time))
    print("Solution Found in {} steps".format(num_of_moves))
else:
    print("No Path Found")

# Plot path data
plt.plot(path)
plt.show()
