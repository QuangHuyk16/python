class Stack:
    def __init__(self):
        self.data = []

    def push(self, element):
        self.data.append(element)

    def pop(self):
        if not self.isEmpty():
            return self.data.pop()

    def isEmpty(self):
        return len(self.data) == 0

    def isFull(self):
        return False

    def count(self):
        return len(self.data)

    def print_stack(self):
        for element in self.data:
            print(element)

# Ví dụ sử dụng lớp Stack
stack = Stack()
stack.push(1.5)
stack.push(2.7)
stack.push(3.9)

stack.print_stack()

