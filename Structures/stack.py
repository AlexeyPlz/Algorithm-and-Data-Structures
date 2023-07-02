class Stack:
    def __init__(self):
        self.values = []

    def push(self, value):
        self.values.append(value)

    def pop(self):
        try:
            return self.values.pop()
        except IndexError:
            raise IndexError("Стек пуст.")

    def size(self):
        return len(self.values)
