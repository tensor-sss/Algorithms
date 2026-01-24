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
