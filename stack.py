class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top_node = None
        self._size = 0

    def push(self, item):
        new_node = Node(item)
        new_node.next = self.top_node
        self.top_node = new_node
        self._size += 1

    def pop(self):
        if not self.top_node:
            raise IndexError("pop from an empty stack")
        popped_item = self.top_node.data
        self.top_node = self.top_node.next
        self._size -= 1
        return popped_item

    def top(self):
        if not self.top_node:
            raise IndexError("top from an empty stack")
        return self.top_node.data

    def size(self):
        return self._size

    def clear(self):
        self.top_node = None
        self._size = 0


stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)

print(f'Size of stack: {stack.size()}')
print(f'Stack top: {stack.top()}')

popped_item = stack.pop()
print("Popped element:", popped_item)

print(f'Size of stack after popping: {stack.size()}')
stack.clear()
print(f'Size of stack after clearing: {stack.size()}')
