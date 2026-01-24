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

def linkedlist_sort(head):
    current = head
    while current and current.next:
        min_node = current
        temp = current.next
        while temp:
            if min_node.data > temp.data:
                min_node = temp
            temp = temp.next
        if min_node != current:
            current.data, min_node.data = min_node.data, current.data
        current = current.next
    return head


l = [3, 55, 44, 20, 7, 202, 101]
head = createLinkedList(l)

sorted_head = linkedlist_sort(head)
printLinkedList(sorted_head)
