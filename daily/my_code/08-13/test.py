import sys
import random
import solution
import solution1
import time


if __name__ == '__main__':
    if len(sys.argv) >= 3:
        row = int(sys.argv[1])
        col = int(sys.argv[2])
        matrix = []
        for i in range(row):
            matrix.append([random.randint(0, 20) for j in range(col)])
    else:
        print('Usage: python %s row col' % __file__)

    start = time.time()
    toBoths, toPacs, toAtls, toNones = solution.find_points(matrix)
    usage = time.time() - start

    print("Points:%d" % len(toBoths))
    print("Solution: usage:  %s" % str(usage))

    start = time.time()
    toBoths = solution1.find_points(matrix)
    usage = time.time() - start

    print("Points:%d" % len(toBoths))
    print("Solution1: usage: %s" % str(usage))