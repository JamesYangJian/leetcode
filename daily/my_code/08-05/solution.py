
class tree_node(object):
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None


def build_tree(pre_order_list, mid_order_list):
    if len(mid_order_list) == 1:
        return tree_node(mid_order_list[0])

    root_val = pre_order_list[0]

    root_idx_in_mid_list = mid_order_list.index(root_val)

    left_mid_list = mid_order_list[0:root_idx_in_mid_list]
    right_mid_list = mid_order_list[root_idx_in_mid_list+1:]

    root = tree_node(root_val)

    if len(left_mid_list) > 0:
        root.left_child = build_tree(pre_order_list[1:1+len(left_mid_list)], left_mid_list)

    if len(right_mid_list) > 0:
        root.right_child = build_tree(pre_order_list[1+len(left_mid_list):], right_mid_list)

    return root

def parse_tree_to_dict(root, ret):
    if not root:
        return

    ret[root.value] = {}
    ret[root.value]['left'] = {}
    ret[root.value]['right'] = {}

    if root.left_child:
        parse_tree_to_dict(root.left_child, ret[root.value]['left'])

    if root.right_child:
        parse_tree_to_dict(root.right_child, ret[root.value]['right'])

    return




if __name__ == '__main__':
    #pre_order_list = [3, 9, 20, 15, 7]
    #mid_order_list = [9, 3, 15, 20, 7]

    pre_order_list = [3, 9, 20, 15, 7]
    mid_order_list = [20, 9, 15, 3, 7]

    tree = build_tree(pre_order_list, mid_order_list)

    ret = {}
    parse_tree_to_dict(tree, ret)

    print(ret)