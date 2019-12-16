

def poker_reverse(A):
    ret = []
    length = len(A)

    for i in range(length-1, -1, -1):
        v = A.pop(i)
        ret.insert(0, v)

        if i != 0:
            v1 = ret.pop(len(ret)-1)
            ret.insert(0, v1)

    return ret


if __name__ == '__main__':
    dst = [1, 3, 5, 7, 9, 10, 2, 4, 6, 8]
    print('dst is {}'.format(dst))

    src = poker_reverse(dst)

    print('src is {}'.format(src))