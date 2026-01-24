# 遍历链表
def print_lnode(head):
    p = head
    while p:
        print(p.data)
        p = p.next

l = [23, 45, 22, 9, 123, 80, 89]

# 3.头插法
class LNode():
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

def head_insertion(l):
    head = LNode()
    for v in l:
        node = LNode(v)
        node.next = head.next
        head.next = node
    return head.next

head = head_insertion(l)
print_lnode(head)