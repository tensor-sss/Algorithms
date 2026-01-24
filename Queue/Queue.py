# enqueue():进队
# dequeue():出队
# peek():访问队头的元素
# if_empty(): 看队空不空

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            return None
    def is_empty(self):
        if len(self.queue) == 0:
            return True
        else:
            return False

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.queue[0]

q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())