'''
这个题是查找一个二叉树中最深叶子节点的最近公共祖先
输入 [1，2，3]为一个二叉树
输出 [1，2，3]列表，第一个元素为查找到的公共祖先, 之后的元素为叶子结点
如果最深叶子节点只有一个，则返回它自己即可

算法思路：
使用分治法，递归函数返回祖先，叶子结点列表，以及叶子结点深度
0. 如果节点为叶子节点，则祖先和叶子节点都是自己，深度为自己的深度，这是递归结束条件
1. 递归左子树，找到最深叶子节点列表，它们的公共祖先，以及叶子节点深度
2. 递归右子树，找到最深叶子节点列表，它们的公共祖先，以及叶子节点深度
3. 判断左右子树的叶子节点深度：
   3.1 左边更深，返回左边结果
   3.2 右边更深，返回右边结果
   3.3 左右深度相同， 合并叶子节点列表，公共祖先为根节点
'''
import math
import sys


def left_child(n):
    return (n<<1) + 1

def right_child(n):
    return (n<<1)+ 2

def get_depth(idx):
    return math.ceil(math.log2(idx+2)) - 1

def find_deepest_child(tree, idx):
    leftChild = left_child(idx)
    rightChild = right_child(idx)
    depth = get_depth(idx)

    if leftChild >= len(tree) and rightChild >= len(tree):
        return idx, [idx], depth

    leftIdx, leftNodes, leftDepth = find_deepest_child(tree, leftChild)

    if rightChild < len(tree):
        rightIdx, rightNodes, rightDepth = find_deepest_child(tree, rightChild)
    else:
        return leftIdx, leftNodes, leftDepth

    if leftDepth > rightDepth:
        return leftIdx, leftNodes, leftDepth
    elif leftDepth < rightDepth:
        return rightIdx, rightNodes, rightDepth
    else:
        leftNodes.extend(rightNodes)
        return idx, leftNodes, leftDepth


def find_common_parent(tree):
    idx, nodes, depth = find_deepest_child(tree, 0)
    ret = [tree[idx]]

    if len(nodes) > 1:
        leaf_nodes  = [tree[i] for i in nodes] 
        ret.extend(leaf_nodes)

    return ret


if __name__ == '__main__':
    if len(sys.argv) < 2:
        count = 5
    else:
        count = int(sys.argv[1])
    tree = [i+1 for i in range(count)]

    ret = find_common_parent(tree)

    print(ret)
    