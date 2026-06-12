class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = ["+","-","*","/"]

        for digit in tokens:
            if stack and digit in operations:
                bottom = stack.pop()
                top = stack.pop()
                if digit == "+":
                    stack.append(top + bottom)
                elif digit == "-":
                    stack.append(top - bottom)
                elif digit == "*":
                    stack.append(top * bottom)
                elif digit == "/":
                    stack.append(int(top / bottom))
            else:
                stack.append(int(digit))
        return int(stack[0])