"""
@file   : 001-preorder.py
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


# 递归写法
def preorder_visit_v1(root):
    if root is not None:
        print(root.value)
        preorder_visit_v1(root.left)
        preorder_visit_v1(root.right)
'''
preorder_visit(1)
preorder_visit(2)
preorder_visit(4)
'''

# 递归写法
def preorder_visit_v2(root):
    result = []
    def preorder_visit(root):
        if root is not None:
            result.append(root.value)
            preorder_visit(root.left)
            preorder_visit(root.right)

    preorder_visit(root)
    return result


# 非递归写法
def preorder_visit_v3(root):
    stack = []
    stack.append(root)   #

    while len(stack) > 0:
        cur_node = stack.pop()
        print(cur_node.value)

        if cur_node.right is not None:
            stack.append(cur_node.right)
        if cur_node.left is not None:
            stack.append(cur_node.left)

if __name__ == '__main__':
    # 1. 得到了一个二叉树
    root = create_binary_tree()

    # 2. 递归先序遍历
    # preorder_visit(root)
    result = preorder_visit_v2(root)
    print(result)

    # 3. 非递归先序遍历


















