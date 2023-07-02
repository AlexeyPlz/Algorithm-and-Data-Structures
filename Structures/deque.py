class Deque:
    def __init__(self, max_size):
        self.elements = [None] * max_size
        self.max_size = max_size
        self.head = 1
        self.tail = 0
        self.size = 0

    def push_back(self, value):
        if self.is_full():
            raise IndexError('Переполнение дека.')
        self.tail = (self.tail + 1) % self.max_size
        self.elements[self.tail] = value
        self.size += 1

    def push_front(self, value):
        if self.is_full():
            raise IndexError('Переполнение дека.')
        self.head = (self.head - 1) % self.max_size
        self.elements[self.head] = value
        self.size += 1

    def pop_back(self):
        if self.is_empty():
            raise IndexError('Дек пуст.')
        value = self.elements[self.tail]
        self.tail = (self.tail - 1) % self.max_size
        self.size -= 1
        return value

    def pop_front(self):
        if self.is_empty():
            raise IndexError('Дек пуст.')
        value = self.elements[self.head]
        self.head = (self.head + 1) % self.max_size
        self.size -= 1
        return value

    def is_full(self):
        return self.size == self.max_size

    def is_empty(self):
        return self.size == 0
