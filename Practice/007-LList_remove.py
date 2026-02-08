# 7. 给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。
class LNode():
    def __init__(self, value=None, next = None):
        self.value = value
        self.next = next

# 用尾插法构建一个链表
def creat_LList(l):
    head = LNode(l[0])
    p = head
    for i in l[1:]:
        node = LNode(i)
        p.next = node
        p = p.next
    return head

# 打印链表
def print_LList(head):
    p = head
    while p:
        print(p.value)
        p = p.next

def LList_remove(head, n):
    if n <= 0:
        raise Exception("n must be greater than 0")
    dummy = LNode()
    dummy.next = head
    fast, slow = dummy, dummy
    for i in range(n):
        if fast.next:
            fast = fast.next
        else:
            raise Exception('out of range')
    while fast.next:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next
    return dummy.next



if __name__ == '__main__':
    l = [1, 3, 53, 2, 243, 22]
    head = creat_LList(l)
    print_LList(head)
    print("*" * 100)
    head = LList_remove(head, 0)
    print_LList(head)
