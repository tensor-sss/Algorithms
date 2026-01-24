# 遍历链表
def print_lnode(head):
    p = head
    while p:
        print(p.data)
        p = p.next

l = [23, 45, 22, 9, 123, 80, 89]

# 2.尾插法
class LNode():
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

def tail_insertion(l):
    head = LNode(l[0])
    p = head
    for v in l[1:]:
        node = LNode(v)
        p.next = node
        p = p.next
    return head

head = tail_insertion(l)
print_lnode(head)




