"""
@file   : 004-layerorder.py
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


def layerorder_v1(root):
    queue = []
    queue.append(root)
    result = []
    while len(queue) > 0:   # 等价于 while queue:
        cur_width = len(queue)
        result.append(cur_width)

        for i in range(cur_width):
            temp = queue.pop(0)
            if temp.left is not None:
                queue.append(temp.left)
            if temp.right is not None:
                queue.append(temp.right)
    # [1]    1
    # [2, 3]  2
    # [4, 5, 6]   3
    res = max(result)
    return res


if __name__ == '__main__':
    root = create_binary_tree()

    result = layerorder_v1(root)
    print(result)



