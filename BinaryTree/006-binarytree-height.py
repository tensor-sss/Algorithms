"""
@file   : 006-binarytree-height.py
@time   : 2026-01-24
"""
# 创建一个二叉树
class BTNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def create_binary_tree():
    root = BTNode("+")
    root.left = BTNode(1)
    root.right = BTNode("*")
    root.right.left = BTNode(2)
    root.right.right = BTNode(3)
    return root


def calc_expression_result(root):
    if str(root.value) in '+-*/':
        left_value = calc_expression_result(root.left)
        right_value = calc_expression_result(root.right)
        if root.value == '+':
            return left_value + right_value
        elif root.value == '-':
            return left_value - right_value
        elif root.value == '*':
            return left_value * right_value
        else:
            return left_value / right_value
    else:
        return root.value


if __name__ == '__main__':
    root = create_binary_tree()
    res = calc_expression_result(root)
    print(res)


