class LNode():
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

def print_list(head):
    p = head
    while p:
        print(p.data)
        p = p.next

l = [1, 3, 5]
s = 4

def tail_insertion(l):
    head = LNode(l[0])
    p = head
    for v in l[1:]:
        node = LNode(v)
        p.next = node
        p = p.next
    return head

def head_insertion(l):
    head = LNode()
    for v in l:
        node = LNode(v)
        node.next = head.next
        head.next = node
    return head.next

head1 = tail_insertion(l)
head2 = head_insertion(l)

# 将s插入l的1，2号位置之间
target1 = LNode(s)
target2 = LNode(s)

# 尾插法
target1.next = head1.next.next
head1.next.next = target1

# 头插法
target2.next = head2.next
head2.next = target2

print_list(head1)
print('*' * 100)
print_list(head2)

# 删除s
head1.next.next = head1.next.next.next
head2.next = head2.next.next

print('*' * 100)
print_list(head1)
print('*' * 100)
print_list(head2)


