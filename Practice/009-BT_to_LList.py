class BTNode():
    def __init__(self, value = None, left = None, right = None ):
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

def preorder(root):
    res = []
    stack = []
    stack.append(root)
    while len(stack) > 0:
        curr_node = stack.pop()
        res.append(curr_node.value)

        if curr_node.right:
            stack.append(curr_node.right)
        if curr_node.left:
            stack.append(curr_node.left)
    return res

def to_LList(l):
    if not l:
        return None

    root = BTNode(l[0])
    curr = root

    for val in l[1:]:
        curr.left = None
        curr.right = BTNode(val)
        curr = curr.right

    return root


if __name__ == '__main__':
    root = create_binary_tree()
    res = preorder(root)
    print(res)
    root = to_LList(res)
    res = preorder(root)
    print(res)
