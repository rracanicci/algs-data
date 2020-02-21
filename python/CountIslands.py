import sys
import matplotlib.pyplot as plt
from   copy              import deepcopy
from   queue             import Queue
from   enum              import Enum

class MapAnalyzer:
    def __init__(self, grid):
        self._grid = grid

    def draw_map(self):
        plt.imshow(self._grid, cmap=plt.cm.Blues)
        plt.show()

    def count_islands(self, mode):
        ans = 0
        grid = deepcopy(self._grid)
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0:
                    getattr(self, mode)(grid, i, j)
                    ans += 1
        return ans

    def dfs(self, grid, i, j):
        # check boudaries
        if (i < 0 or i >= len(grid) or
            j < 0 or j >= len(grid[i]) or 
            grid[i][j] == 1): return

        # mark as visited
        grid[i][j] = 1

        # spread to neighbours
        for dir_i, dir_j in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            self.dfs(grid, i + dir_i, j + dir_j)

    def bfs(self, grid, i, j):
        q = Queue()
        # insert current node
        q.put_nowait((i, j))

        # keep going while there are neighbours
        while not q.empty():
            curr_i, curr_j = q.get_nowait()

            # mark as visited
            grid[curr_i][curr_j] = 1

            # spread to neighbours
            for dir_i, dir_j in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                next_i, next_j = curr_i + dir_i, curr_j + dir_j

                # check boudaries
                if (next_i >= 0 and next_i < len(grid) and
                    next_j >= 0 and next_j < len(grid[next_i]) and 
                    grid[next_i][next_j] != 1): q.put_nowait((next_i, next_j))

def main():
    # 1 -> means water
    # 0 -> means ground
    an = MapAnalyzer([
        [1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0],
        [1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0],
        [1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0],
        [0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0],
        [0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1],
        [1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0],
        [1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0],
        [1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0],
        [0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1],
        [1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1],
        [1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1],
        [1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1],
        [0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1],
    ])

    an.draw_map()
    print('bfs', an.count_islands('bfs'))
    print('dfs', an.count_islands('dfs'))

    return 0

if __name__ == '__main__': sys.exit(main())