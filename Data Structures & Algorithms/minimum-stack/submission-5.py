class MinStack:

    def __init__(self):
        self.minval = int()
        self.stack = list()

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.stack) == 1:
            self.minval = val
        else:
            self.minval = min(self.minval, val)

    def pop(self) -> None:
        if self.top() == self.minval:
            self.minval = min(self.stack[:-1], default=None)
        self.stack = self.stack[:-1]

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        if len(self.stack) != 0:
            return self.minval
        return 0