# 6. 给你两个单链表的头节点 headA 和 headB ，请你找出并返回两个单链表相交的起始节点。如果两个链表不存在相交节点，返回 null 。
# 双指针法
# 1  2  3  5  8  9  2
# 4  5  8  9  2
# 1  2  3  5  8  9  2  4  5  8  9  2
# 4  5  8  9  2  1  2  3  5  8  9  2
# 可以看到二者同时到达了交点5处

class LNode():
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next

def creat_LList(l):
    head = LNode(l[0])
    p = head
    for i in l[1:]:
        node = LNode(i)
        p.next = node
        p = p.next
    return head


def connect_LLists(l, head):
    head1 = LNode(l[0])
    p = head1
    for i in l[1:]:
        node = LNode(i)
        p.next = node
        p = p.next
    p.next = head
    return head1

def print_LList(head):
    p = head
    while p:
        print(p.value)
        p = p.next

def find_Intersect(head1, head2):
    if not head1 or not head2:
        return None
    p1 = head1
    p2 = head2
    while p1 != p2:
        if p1:
            p1 = p1.next
        else:
            p1 = head2
        if p2:
            p2 = p2.next
        else:
            p2 = head1
    return p1



if __name__ == '__main__':

    l = [ 3, 5, 7, 44]
    l1 = [2, 4, 5]
    l2 = [5, 2, 1, 3, 6, 9]
    head = creat_LList(l)
    test = creat_LList(l2)
    head1 = connect_LLists(l1, head)
    head2 = connect_LLists(l2, head)
    print_LList(head1)
    print('*' * 100)
    print_LList(head2)
    print('*' * 100)
    print_LList(head)
    print('*' * 100)
    res = find_Intersect(head1, head2)
    print(res.value)
    print('*' * 100)
    print_LList(res)
    print('*' * 100)
    res1 = find_Intersect(head, test)
    print(res1)



