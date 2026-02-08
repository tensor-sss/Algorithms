class BTNode():
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right



def lowest_common_ancestor(root, node1, node2):
    if root == node1 or root == node2:
        return root

    if root is None:
        return root

    left = lowest_common_ancestor(root.left, node1, node2)
    right = lowest_common_ancestor(root.right, node1, node2)
    if left and right:
        return root
    elif left:
        return left
    else:
        return right


def create_binary_tree():
    root = BTNode(1)
    root.left = BTNode(2)
    root.right = BTNode(3)
    root.left.left = BTNode(4)
    root.left.right = BTNode(5)
    root.right.right = BTNode(6)
    return root


root = create_binary_tree()
node1 = root.left.left
node2 = root.left

res = lowest_common_ancestor(root, node1, node2)
print(res)



