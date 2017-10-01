class Node():
    __slots__ = ['next_node', 'value']

    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

class Stack():
    
    def __init__(self):
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size

    def push(self, value):
        self._head = Node(value, self._head)
        self._size += 1
        return self

    def pop(self):
        if self._head is None:
            raise IndexError('Stack is empty')
        value = self._head.value
        self._head = self._head.next_node
        self._size -= 1
        return value

    def peek(self):
        if self._head is None:
            return None
        return self._head.value

    def isEmpty(self):
        return self._head is None
