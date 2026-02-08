"""
@file   : 006-is_Symmetry_Tree.py
@time   : 2026-02-08
"""
class BTNode():
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right



def create_binary_tree():
    root = BTNode(1)
    root.left = BTNode(2)
    root.right = BTNode(2)
    root.left.left = BTNode(4)
    root.left.right = BTNode(5)
    root.right.left = BTNode(5)
    root.right.right = BTNode(5)
    return root


def is_symmetry_tree(root):
    def func(left, right):
        if left is None and right is None:  # 两者空
            return True

        if left is None or right is None:  # 一者空
            # 一个空 一个不空
            return False

        return left.value == right.value and func(left.left, right.right) and func(left.right, right.left)

    if root is None:
        return True

    return func(root.left, root.right)


root = create_binary_tree()
res = is_symmetry_tree(root)
print(res)



