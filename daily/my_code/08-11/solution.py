"""
To find the friend circles from a matrix, use below steps:

1. Iterate each row which represents the friends of on person
   1.1 Iterate each col in the row, if the col hasn't been handled yet and value is 1, 
       merge two rows, add col in to handled_list, then iterate from beginning
   1.2 After the last col of the row has been handled, add row to circle_list and go to next unhandled row

2. return cicrle list
"""

def list_or(l1, l2):
    if len(l1) != len(l2):
        return None

    ret = []
    for i in range(len(l1)):
        ret.append(l1[i] or l2[i])

    return ret


def find_friend_circles(relations):
    try:
        rows = len(relations)
        cols = len(relations)

        if rows != cols:
            raise Exception("Not a valid relation matrix")
    except Exception as e:
        print("Error: %s " % str(e))
        return None

    handledRows = []
    circles = []

    for i in range(rows):
        if i in handledRows:
            continue

        rowFinished = False
        handledRows.append(i)
        while not rowFinished:
            for j in range(cols):
                if relations[i][j] == 0 or j in handledRows:
                    continue
                else:
                    relations[i] = list_or(relations[i], relations[j])
                    handledRows.append(j)
                    break
            else:
                rowFinished = True
        circles.append(relations[i])

    return circles

if __name__ == '__main__':
    relations = [[1, 0, 1, 0, 0],
                 [0, 1, 1, 0, 1],
                 [1, 1, 1, 0, 0],
                 [0, 0, 0, 1, 0],
                 [0, 1, 0, 0, 1]]


    circles = find_friend_circles(relations)

    print(circles)

