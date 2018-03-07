class Node():
    __slots__ = ['value', 'next_node']

    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

class LinkedList():
    def __init__(self):
        self._head = None
        self._length = 0

    def add(self, value):
        self._head = Node(value, self._head)
        self._length += 1
        return self

    def pop(self):
        if self._head is None:
            raise IndexError('Linked list is empty')
        cur = self._head
        self._head = self._head.next_node
        self._length -= 1
        return cur.value

    def search(self, value):
        cur = self._head
        while cur:
            if cur.value == value:
                return True
            cur = cur.next_node
        return False

    def index(self, value):
        cur = self._head
        index = 0
        while cur:
            if cur.value == value:
                return index
            index += 1
            cur = cur.next_node
        else:
            return -1

    def remove(self, value):
        cur = self._head
        prev = None
        while cur:
            if cur.value == value:
                if prev is None:
                    self._head = self._head.next_node
                else:
                    prev.next_node = cur.next_node
            prev, cur = cur, cur.next_node

    @property
    def length(self):
        return self._length

    def isEmpty(self):
        return self._head is None

    def __str__(self):
        if self._head is None:
            return 'None'
        cur = self._head
        values = []
        while cur:
            values.append(str(cur.value))
            cur = cur.next_node
        return ' -> '.join(values) + ' -> None'


    def __getitem__(self, index):
        if 0 <= index < self._length:
            cur = self._head
            for _ in range(index):
                cur = cur.next_node
            return cur.value
        raise IndexError('Index out of range')

