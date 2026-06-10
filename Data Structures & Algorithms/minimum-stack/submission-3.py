class MinStack:

    def __init__(self):
        self.stack =  []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        
    def top(self) -> int:
        top = self.stack[-1]
        return top

    def getMin(self) -> int:
        check = []
        for num in self.stack:
            if isinstance(num,int):
                check.append(num)
            else:
                continue
        min_elm = min(check)
        return min_elm
        
