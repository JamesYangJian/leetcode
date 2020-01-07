# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.max_length = 0

    def path_calc(self, node: TreeNode) -> int:
        if not node:
            return 0

        l = self.path_calc(node.left)
        r = self.path_calc(node.right)

        lCount = 0
        rCount = 0

        if node.left and node.left.val == node.val:
            lCount = l + 1
        if node.right and node.right.val == node.val:
            rCount = r + 1

        tmp_len = lCount + rCount

        self.max_length = self.max_length if self.max_length > tmp_len else tmp_len

        return lCount if lCount > rCount else rCount


    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.path_calc(root)

        return self.max_length

def create_left_child(node: TreeNode, val:int) -> TreeNode:
    lChild = TreeNode(val)
    node.left = lChild

    return lChild

def create_right_child(node: TreeNode, val:int) -> TreeNode:
    rChild = TreeNode(val)
    node.right = rChild

    return rChild

if __name__ == '__main__':
    solution = Solution()

    root = TreeNode(5)

    node = create_left_child(root, 5)
    create_left_child(node, 5)
    create_right_child(node, 3)

    node = create_right_child(root, 5)
    create_left_child(node, 4)
    create_right_child(node, 5)

    length = solution.longestUnivaluePath(root)
    print("The longest path in this tree is {}".format(length))

