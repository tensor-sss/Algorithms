# 创建一个二叉树
class BTNode():
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

def create_BT():
    root = BTNode(1)
    root.left = BTNode(2)
    root.right = BTNode(3)
    root.left.left = BTNode(4)
    root.left.right = BTNode(5)
    root.right.left = BTNode(6)
    root.right.right = BTNode(7)
    return root

# 中序遍历：依照左，中，右的顺序
# 方法一：递归写法
def mid_order_1(root, result):

    if root is not None:
        mid_order_1(root.left, result)
        result.append(root.value)
        mid_order_1(root.right, result)
    return result

# 方法二：
def mid_order_2(root):
    # 用 stack 来手动保存父节点，以便访问完左子树后回溯
    stack = []
    # 实现一个指针，用来追踪遍历的位置
    curr_node = root
    # 创建一个空列表，用来保存结果
    result = []
    # 终止条件只要遍历路径还没完全走完（当前节点未空 或 回溯路径未清空），中序遍历就必须继续。
    while curr_node is not None or len(stack) > 0:
        while curr_node is not None:
            # 将节点的左带进来
            # 保存当前节点作为“回溯点”，并持续深入左子树，模拟中序遍历中的递归调用过程。
            stack.append(curr_node)
            curr_node = curr_node.left
        # 左子树走到尽头，开始回溯
        curr_node = stack.pop()
        # 左子树已完成，访问当前节点（中序的“根”）
        result.append(curr_node.value)
        # 继续向右走,向右子树，继续中序遍历
        curr_node = curr_node.right
    # 将结果返回
    return result



if '__main__' == __name__:
    root = create_BT()
    res = []
    res = mid_order_1(root, res)
    print(res)
    res = mid_order_2(root)
    print(res)
