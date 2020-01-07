"""
1. Use dynamic programming, make matrix for src and dst string

2. Check the matrix by DFS to see if dst is a substring of src

3. Iterate dictionary, check the next word if it's longer than current max string

"""

import copy



def check_matrix(row, col, matrix):
    for i in range(row, len(matrix)):
        if matrix[row][col] == 1:

            if col == len(matrix[0]) - 1:
                return True
            
            ret = check_matrix(i+1, col+1, matrix)
            if ret:
                return True
    return False


def check_dst_in_src(src, dst):
    if len(src) == 0 or len(dst) == 0:
        return False

    matrix = [[0 for i in range(len(dst))] for j in range(len(src))]

    for i in range(len(dst)):
        for j in range(len(src)):
            if src[j] == dst[i]:
                matrix[j][i] = 1


    ret = check_matrix(0, 0, matrix)

    if ret:
        print("String:%s contains String:%s" % (src, dst))
        return True
    else:
        print("Dst is not a Substring of Src!")
        return False

def find_longest_string_in_dict(src_str, word_list):
    max_idx = -1
    max_len = 0
    for idx in range(len(word_list)):
        dst_str = word_list[idx]
        if len(dst_str) <= max_len:
            continue
        else:
            ret = check_dst_in_src(src_str, dst_str)
            if ret:
                max_idx = idx
                max_len = len(dst_str)

    if max_idx != -1:
        return max_idx, word_list[max_idx]
    else:
        return -1, ''



if __name__ == '__main__':
    src = 'abpcplea'
    word_list = ["ale","apple","monkey","plea"]
    word_list = ["a","b","c","d"]

    idx, ret = find_longest_string_in_dict(src, word_list)

    print("Index: {}, ret: {}".format(idx, ret))
