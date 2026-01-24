# 构建链表
# 1.直接连接节点构造链表
class LNode:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

l1 = LNode(1)
l2 = LNode(3)
l3 = LNode(5)

l1.next = l2
l1.next.next = l3

# 遍历链表
def print_lnode(head):
    p = head
    while p:
        print(p.data)
        p = p.next
print_lnode(l1)

