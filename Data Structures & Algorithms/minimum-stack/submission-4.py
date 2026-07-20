class MinStack:

    def __init__(self):
        self.stack = []
        self.tops = -1
        self.minimum = None

    def push(self, val: int) -> None:
        self.tops += 1
        
        if self.minimum == None:
            self.minimum = val

        elif val < self.minimum:
            self.minimum = val


        return self.stack.append(val)

    def pop(self) -> None:
        val = self.stack[self.tops]
        self.tops -= 1
        self.stack.pop()
        if val == self.minimum:

            self.minimum = min(self.stack) if self.stack else None

        return None

    def top(self) -> int:
        return self.stack[self.tops]

    def getMin(self) -> int:

        return self.minimum
