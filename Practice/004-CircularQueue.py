# 3. 自己做一个循环队列。 循环队列指的是 最后一个节点的下一个节点是头结点。  要求: 支持在常数时间复杂度内完成入队、出队、获取队首/队尾元素操作。
class CircularQueue:
    def __init__(self, k):
        self.queue = [None] * (k + 1)
        self.front = 0
        self.rear = 0
        self.capacity = k + 1

    def is_empty(self):
        return self.front == self.rear

    def is_full(self):
        return (self.rear + 1) % self.capacity == self.front

    def enqueue(self, x):
        if self.is_full():
            raise Exception('Queue is full')
        self.queue[self.rear] = x
        self.rear = (self.rear + 1) % self.capacity

    def dequeue(self):
        if self.is_empty():
            raise Exception('Queue is empty')
        x = self.queue[self.front]
        self.front = (self.front + 1) % self.capacity
        return x

    def get_front_elem(self):
        return self.queue[self.front]

    def get_rear_elem(self):
        return self.queue[self.rear-1]


