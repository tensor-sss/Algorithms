"""
@file   : 007-binary_sort_tree.py
@time   : 2026-01-24
"""
# 创建一个二叉树
class BTNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# 增删改查
# 二叉排序树   二叉搜索树   是一个东西
class BinarySortTree:
    def __init__(self, root=None):
        self.root = root

    def insert_node(self, key):
        node = BTNode(key)
        if self.root is None:
            self.root = node
        else:
            self.insert(self.root, node)

    def insert(self, root, node):
        if node.value < root.value:
            if root.left is None:
                root.left = node
            else:
                self.insert(root.left, node)
        else:
            if root.right is None:
                root.right = node
            else:
                self.insert(root.right, node)

    def search_node(self, key):
        # 找key这个值  如果存在返回True 不存在返回False
        return self.search(self.root, key)

    def search(self, root, key):
        if root is None:
            return False
        elif root.value == key:
            return True
        elif root.value < key:
            return self.search(root.right, key)
        else:
            return self.search(root.left, key)

    def delete_node(self, key):
        self.root = self.delete(self.root, key)

    def delete(self, root, key):
        if root.value > key:
            root.left = self.delete(root.left, key)
        elif root.value < key:
            root.right = self.delete(root.right, key)
        else:
            if root.left is None and root.right is None:
                return None

            if root.left is None:
                return root.right

            if root.right is None:
                return root.left

            # 两个都不空的情况
            mid_node = self.get_max_value(root.left)
            root.value = mid_node.value
            root.left = self.delete(root.left, mid_node.value)
        return root


    def get_max_value(self, root):
        while root.right is not None:
            root = root.right
        return root

    def midorder(self):
        result = []
        def f1(root):
            if root is not None:
                f1(root.left)
                result.append(root.value)
                f1(root.right)
        f1(self.root)
        return result



root = BinarySortTree()
l1 = [43, 12, 54, 65, 23, 52, 15]
for v in l1:
    root.insert_node(v)

# res = root.midorder()

# res = root.search_node(24)
# print(res)

print(root.midorder())  # [12, 15, 23, 43, 52, 54, 65]
root.delete_node(43)
print(root.midorder())









