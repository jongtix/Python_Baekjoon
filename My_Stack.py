class MyStack:
    stack = []

    def __init__(self):
        self.stack = []

    def push(self, X):
        self.stack.append(X)

    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            return None

    def size(self):
        return len(self.stack)

    def empty(self):
        if self.stack:
            return True
        else:
            return False

    def top(self):
        if self.stack:
            return self.stack[-1]
        else:
            return None