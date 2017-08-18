class Stack(object):
    """ Stack implementation | (C) @ Bofin Babu"""
    def __init__(self):
        self.elements = []

    def pop(self):
        return self.elements.pop()

    def push(self, item):
        self.elements.append(item)

    def is_empty(self):
        return self.elements == []

    def size(self):
        return len(self.elements)
