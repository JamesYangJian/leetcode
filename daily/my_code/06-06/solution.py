"""
Find the max wait days in a row


Initial condition: the last element is zero according to the requirement
The main thinking is
1. record the index of biggest value in the list, default is the last one
2. iterate the list in reverse order from the 2nd least index
3. if value of cur index is less than its bigger neighbour, then only need to wait 1 day
   else:
    if value of cur index is bigger than its bigger neighbour, and it's bigger than the current biggest one, then, it will wait 0 days, and mark this idx as the biggest index
    if value is less than biggest one, then iterate between its bigger neighbour and the biggest index, to find the first value bigger than it

"""


def find_max_wait_day(A):
    length = len(A)
    cur_last_idx = length - 1
    result = [0 for i in range(0, length)]

    for i in range(length - 2, -1, -1):
        if A[i] < A[i + 1]:
            result[i] = 1
        else:
            if A[i] > A[cur_last_idx]:
                result[i] = 0
                cur_last_idx = i
            else:
                for j in range(i + 2, cur_last_idx + 1, 1):
                    if A[i] < A[j]:
                        result[i] = j - i

    return result


if __name__ == '__main__':
    A = [22, 33, 20, 5, 6, 7, 40, 32, 41, 50, 12, 18]

    print(A)

    ret = find_max_wait_day(A)

    print(ret)
