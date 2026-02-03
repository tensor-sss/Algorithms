# 记录一下，学到了一种新的范式：入口函数负责处理边界条件和对象状态，递归辅助函数负责维护数据结构的不变式。
# 第一步：构建一个类，实现创建二叉树的节点（需要三个参数：当前节点的值，左节点，右节点）
# AI完善版设计一个节点构造函数，用于创建二叉树的基本节点结构。该函数包含三个参数：节点值 value、左子节点 left 和右子节点 right，
# 其中左右子节点可以为空，用以表示叶子节点。
class BTNode():
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

# 创建二叉排序树（又名二叉搜索树）
class BinarySortTree():

    # 初始化根节点
    def __init__(self, root = None):
        self.root = root

    # 实现插入功能，采用「入口函数 + 递归实现函数」模式
    def insert_node(self, value):
        #创建一个新的二叉树节点，并在初始化时将 value 赋值给该节点的值域
        node = BTNode(value)
        # 如果当前根节点内的值为None，直接插入根节点
        if self.root is None:
            self.root = node
        else:
            self.insert(self.root, node)
    # 插入时应保证二叉搜索树的性质，即左子树的所有节点值小于当前节点，右子树的所有节点值大于当前节点
    def insert(self, root, node):
        if node.value < root.value:
            if root.left is None:
                root.left = node
            else:
                self.insert(root.left, node) # 递归
        else:
            if root.right is None:
                root.right = node
            else:
                self.insert(root.right, node)
    # 接下来实现搜索的逻辑
    def search_node(self, value):
        return self.search(self.root, value)

    def search(self, root, value):
        # 先看根节点的情况
        if root is None:
            return False
        elif root.value == value:
            return True
        elif root.value < value:
            return self.search(root.right, value)
        else:
            return self.search(root.left, value)

    # 接下来实现删除的逻辑
    def delete_node(self, value):
        self.root = self.delete(self.root, value)

    def delete(self, root, value):
        if root is None:
            return None
        # 如果要删除的值比当前节点大，那么就向右边找
        if root.value < value:
            root.right = self.delete(root.right, value)
        # 若小，找左边
        elif root.value > value:
            root.left = self.delete(root.left, value)
        # 若相等，则说明找到要删除的那个值，进一步完善删除逻辑
        else:
            # 这里分三种情况，一种是要删除的值左右边两边都没有子节点，一种是左边有或右边有，最后一种是左右两边都有
            if root.left is None and root.right is None:
                # 最简单的情况，直接删掉该节点
                return None
            elif root.left is None:
                # 无论是只有左节点还是只有右节点，直接将剩余的节点拉上来覆盖当前节点即可
                return root.right
            elif root.right is None:
                return root.left
            else:
                # 最复杂的情况，及两边都存在，我们需要将左边节点中最大的值拉上来替代当前节点的值并删去原左边节点最大值
                # 找到并备份左边最大的值
                mid_node = self.find_left_max(root.left)
                root.value = mid_node.value
                root.left = self.delete(root.left, mid_node.value)

            return root
    '''
    递归版
    def find_left_max(self, root):
        if root.right is None:
            return root
        else:
            return self.find_left_max(root.right)
    '''

    # 迭代版
    def find_left_max(self, root):
        while root.right:
            root = root.right
        return root

    # 按照中序遍历的逻辑构建函数，使得打印出的值刚好从小到大排序
    def mid_order(self):
        result = []
        def f(root):
            if root is not None:
                f(root.left)
                result.append(root.value)
                f(root.right)
        f(self.root)
        return result

if __name__ == '__main__':
    root = BinarySortTree()
    l1 = [43, 12, 54, 65, 23, 52, 15]
    for v in l1:
        root.insert_node(v)

    # res = root.mid_order()

    # res = root.search_node(24)
    # print(res)

    print(root.mid_order())  # [12, 15, 23, 43, 52, 54, 65]
    root.delete_node(43)
    print(root.mid_order())







