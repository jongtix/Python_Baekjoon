from collections import deque


class MyQueue:
    queue = deque()

    def __init__(self):
        self.queue = deque()

    def push(self, X):
        self.queue.append(X)

    def pop(self):
        if self.queue:
            return self.queue.popleft()
        else:
            return None

    def size(self):
        if self.queue:
            return len(self.queue)
        else:
            return None

    def empty(self):
        if self.queue:
            return False
        else:
            return True

    def front(self):
        if self.queue:
            return self.queue[0]
        else:
            return None

    def back(self):
        if self.queue:
            return self.queue[-1]
        else:
            return None