class Queue(object):
    """ Queue implementation | (C) @ Bofin Babu"""
    def __init__(self):
        self.elements = []

    def enQ(self, item):
        self.elements.append(item)

    def deQ(self):
        return self.elements.pop(-len(self.elements))

    def is_empty(self):
        return self.elements == []

    def size(self):
        return len(self.elements)