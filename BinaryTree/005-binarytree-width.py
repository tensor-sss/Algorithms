"""
@file   : 005-binarytree-width.py
@time   : 2026-01-24
"""
# 创建一个二叉树
class BTNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def create_binary_tree():
    root = BTNode(1)
    root.left = BTNode(2)
    root.right = BTNode(3)
    root.left.left = BTNode(4)
    root.left.right = BTNode(5)
    root.right.right = BTNode(6)
    return root


# 借鉴层序遍历
def get_binarytree_width(root):



    pass



if __name__ == '__main__':
    root = create_binary_tree()

    res = get_binarytree_width(root)
    print(res)
