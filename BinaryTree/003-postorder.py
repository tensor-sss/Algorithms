"""
@file   : 003-postorder.py
@time   : 2026-01-23
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


def postorder_visit_v1(root):
    if root is not None:
        postorder_visit_v1(root.left)
        postorder_visit_v1(root.right)
        print(root.value)


def postorder_visit_v2(root):
    stack = []
    stack.append(root)   #

    result = []
    while len(stack) > 0:
        cur_node = stack.pop()
        result.append(cur_node.value)
        if cur_node.left is not None:
            stack.append(cur_node.left)
        if cur_node.right is not None:
            stack.append(cur_node.right)
    return result[::-1]


if __name__ == '__main__':
    # 1. 得到了一个二叉树
    root = create_binary_tree()

    # 2. 后续遍历
    # postorder_visit_v1(root)

    # 3. 非递归后序遍历
    result = postorder_visit_v2(root)
    print(result)

