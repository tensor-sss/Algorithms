"""
@file   : 002-midorder.py
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


# 递归实现
def midorder_visit_v1(root):
    if root is not None:
        midorder_visit_v1(root.left)
        print(root.value)
        midorder_visit_v1(root.right)


# 非递归实现
def midorder_visit_v2(root):
    cur_node = root
    stack = []
    result = []
    while cur_node is not None or len(stack) > 0:

        # 这一层循环  把当前节点的所有左带进来
        while cur_node is not None:
            stack.append(cur_node)
            cur_node = cur_node.left
        # stack = [1, 2, 4]

        cur_node = stack.pop()
        result.append(cur_node.value)
        cur_node = cur_node.right
        # stack = [1, 2, 4]
    return result


if __name__ == '__main__':
    # 1. 得到了一个二叉树
    root = create_binary_tree()

    # 2. 中序遍历
    # midorder_visit_v1(root)

    # 3. 非递归中序遍历
    result = midorder_visit_v2(root)
    print(result)





