class Queue:
    def __init__(self, max_size):
        self.queue = [None] * max_size
        self.max_size = max_size
        self.head = 0
        self.tail = 0
        self.size = 0

    def push(self, value):
        if self.is_full():
            raise IndexError('Переполнение очереди.')
        self.queue[self.tail] = value
        self.tail = (self.tail + 1) % self.max_size
        self.size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError('Очередь пуста.')
        value = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_size
        self.size -= 1
        return value

    def is_full(self):
        return self.size == self.max_size

    def is_empty(self):
        return self.size == 0
