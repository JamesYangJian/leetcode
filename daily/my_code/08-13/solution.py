import time
import sys
import random

"""
Simply use dfs to iterate all points, to see if it can reach both pacific and atlantic
"""

class Point(object):
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.neighbourNum = 4

        self.get_neighour = [self.left, self.up, self.right, self.down]

    def neighbour(self, idx):
        if idx < 0 or idx >= self.neighbourNum:
            raise Exception("invalid neighbour index")

        return self.get_neighour[idx]()

    def left(self):
        return (self.row, self.col-1)

    def up(self):
        return (self.row-1, self.col)

    def right(self):
        return (self.row, self.col+1)

    def down(self):
        return (self.row+1, self.col)



def dfs_path(matrix, row, col, visited, toPac=False, toAtl=False):
    total_row = len(matrix)
    total_col = len(matrix[0])
    if row == 0 or col == 0:
        toPac = True

    if row == total_row-1 or col == total_col-1:
        toAtl = True

    if toPac and toAtl:
        return True, toPac, toAtl

    pt = Point(row, col)

    for i in range(pt.neighbourNum):
        next_pt = pt.neighbour(i)

        if next_pt[0] < 0 or next_pt[0] >= total_row or next_pt[1] < 0 or next_pt[1] >= total_col:
            continue

        if (next_pt[0], next_pt[1]) in visited:
            continue

        if matrix[row][col] < matrix[next_pt[0]][next_pt[1]]:
            continue

        visited.append((next_pt[0], next_pt[1]))
        ret, toPac, toAtl = dfs_path(matrix, next_pt[0], next_pt[1], visited, toPac, toAtl)

        if ret:
            return ret, toPac, toAtl

    return False, toPac, toAtl


def find_points(matrix):
    total_row = len(matrix)
    total_col = len(matrix[0])
    visited = []
    toBoths = []
    toPacs = []
    toAtls = []
    toNones = []
    for i in range(total_row):
        for j in range(total_col):
            visited = []
            ret, toPac, toAtl = dfs_path(matrix, i, j, visited)
            if ret:
                toBoths.append((i, j))
            elif toPac:
                toPacs.append((i, j))
            elif toAtl:
                toAtls.append((i, j))
            else:
                toNones.append((i, j))

    return toBoths, toPacs, toAtls, toNones

if __name__ == '__main__':
    if len(sys.argv) >= 3:
        row = int(sys.argv[1])
        col = int(sys.argv[2])
        matrix = []
        for i in range(row):
            matrix.append([random.randint(0, 20) for j in range(col)])
    else:
        matrix = [[1, 2, 2, 3, 5],
                  [3, 2, 3, 4, 4],
                  [2, 4, 5, 3, 1],
                  [6, 7, 1, 4, 5],
                  [5, 1, 1, 2, 4]]
    start = time.time()
    toBoths, toPacs, toAtls, toNones = find_points(matrix)
    usage = time.time() - start

    print("toBoth: %s" % str(toBoths))
    #print("toPac: %s" % str(toPacs))
    #print("toAtl: %s" % str(toAtls))
    #print("toNone: %s" % str(toNones))
    print("usage: %s" % str(usage))



