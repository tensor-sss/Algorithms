class LNode():
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

def createLinkedList(l):
    head = LNode(l[0])
    p = head
    for v in l[1:]:
        node = LNode(v)
        p.next = node
        p = p.next
    return head

def printLinkedList(head):
    p = head
    while p:
        print(p.data)
        p = p.next

def mergeSort(head1, head2):
    p1 = head1
    p2 = head2
    head = LNode()
    p = head
    while p1 and p2:
        if p1.data < p2.data:
            # 将要加入的节点与后面的进行分割
            temp = p1
            p1 = p1.next
            temp.next = None # 完成分割
            p.next = temp
            p = p.next
        else:
            temp = p2
            p2 = p2.next
            temp.next = None
            p.next = temp
            p = p.next
    if p1 is None:
        p.next = p2
    else:
        p.next = p1

    return head.next

l1 = [3, 6, 9, 22, 55]
l2 = [4, 7, 8, 31, 77]

head1 = createLinkedList(l1)
head2 = createLinkedList(l2)

head = mergeSort(head1, head2)
printLinkedList(head)