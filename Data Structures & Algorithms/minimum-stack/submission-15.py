class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()

    def top(self) -> int:
        if not self.stack:
            return 0
        top = self.stack[-1]
        return top

    def getMin(self) -> int:
        min_val = []
        for num in self.stack:
            if isinstance(num, int):
                min_val.append(num)
            else:
                continue
        min_elm = min(min_val)
        return min_elm if min_val else 0
        
