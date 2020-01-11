import time
import sys
import random

"""
Use dfs to iterate points to see if it can reach both pacific and atlantic
Exclude the points in the path which can reach both pacific and atlantic
Excluce the neighbours which can reach neither pacific nor atlantic

Through testing, solution1 save about 1/3 time usage compared to solution

(base) yangjiandeMacBook-Pro:08-13 yangjian$ python test.py 500 1000
Points:18
Solution: usage:  16.690646171569824
Points:18
Solution1: usage: 10.090618133544922
(base) yangjiandeMacBook-Pro:08-13 yangjian$ python test.py 500 1000
Points:6
Solution: usage:  16.794503211975098
Points:6
Solution1: usage: 10.140045642852783
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


def dfs_path(matrix, row, col, visited, path, toPacs, toAtls, toBoths, toNone, toPac=False, toAtl=False):
    total_row = len(matrix)
    total_col = len(matrix[0])
    if row == 0 or col == 0:
        toPac = True
        toPacs.update(set(path))

    if row == total_row-1 or col == total_col-1:
        toAtl = True
        toAtls.update(set(path))

    if toPac and toAtl:
        #print("merge: toBoths:%s, toPacs:%s, toAtls:%s" % (str(toBoths), str(toPacs), str(toAtls)))
        toBoths.update(toPacs.intersection(toAtls))
        return True, toPac, toAtl

    pt = Point(row, col)

    for i in range(pt.neighbourNum):
        next_pt = pt.neighbour(i)

        if next_pt[0] < 0 or next_pt[0] >= total_row or next_pt[1] < 0 or next_pt[1] >= total_col:
            continue

        if (next_pt[0], next_pt[1]) in visited:
            continue

        if (next_pt[0], next_pt[1]) in toNone:
            continue

        if matrix[row][col] < matrix[next_pt[0]][next_pt[1]]:
            continue

        visited.append((next_pt[0], next_pt[1]))
        path.append((next_pt[0], next_pt[1]))
        ret, toPac, toAtl = dfs_path(matrix, next_pt[0], next_pt[1], visited, path, toPacs, toAtls, toBoths, toNone, toPac, toAtl)

        if ret:
            return ret, toPac, toAtl
        else:
            path.pop(len(path)-1)

    return False, toPac, toAtl


def find_points(matrix):
    total_row = len(matrix)
    total_col = len(matrix[0])
    visited = []
    toBoths = set()
    toNone = set()
    for i in range(total_row):
        for j in range(total_col):
            #print("row:%d, col:%d, toBoths:%s" % (i, j, str(toBoths)))
            if (i, j) in toBoths:
                #print("skip a point")
                continue
            visited = []
            toPacs = set()
            toAtls = set()
            curPath = [(i, j)]
            ret, toPac, toAtl = dfs_path(matrix, i, j, visited, curPath, toPacs, toAtls, toBoths, toNone)
            if not ret and not toPac and not toAtl:
                toNone.add((i, j))

                

    return toBoths

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
    toBoths = find_points(matrix)
    usage = time.time() - start
    print("Final: toBoth: %s" % str(toBoths))
    print("Usage:%s" % str(usage))
    #print("toPac: %s" % str(toPacs))
    #print("toAtl: %s" % str(toAtls))
    #print("toNone: %s" % str(toNones))



