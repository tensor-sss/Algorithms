class LNode():
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next
def print_linked_list(head):
    p = head
    while p:
        print(p.data)
        p = p.next

def create_circle_linked_list(l):
    head = LNode(l[0])
    p = head
    for v in l[1:]:
        node = LNode(v)
        p.next = node
        p = p.next
    p.next = head
    return head

def check_circle(head):
    slow = head
    fast = head.next
    while not (fast == slow or fast is None):
        slow = slow.next
        if fast.next is None:
            fast = None
        else:
            fast = fast.next.next

    if fast == slow:
        print("Circle found")
    else:
        print("Circle is not found")


l = [3, 5, 99, 23, 5, 12, 53, 76, 0]

head = create_circle_linked_list(l)

check_circle(head)
