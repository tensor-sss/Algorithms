# push
# pop
# is_empty()
# get_current_size

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return None

    def is_empty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False

    def get_current_size(self):
        return len(self.stack)

s = Stack()
s.push(10)
s.push(20)
s.push(30)
print(s.pop())
print(s.pop())
print(s.pop())
print(s.get_current_size())