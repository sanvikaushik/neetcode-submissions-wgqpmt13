class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        if len(self.stack) == 0 or len(self.min_stack) == 0:
            self.stack.append(val)
            self.min_stack.append(val)
        else:
            self.stack.append(val)

        if val <= self.min_stack[-1]:
            self.min_stack.append(val)


    def pop(self) -> None:
        if self.stack[-1] == self.min_stack[-1]:
            self.min_stack.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
