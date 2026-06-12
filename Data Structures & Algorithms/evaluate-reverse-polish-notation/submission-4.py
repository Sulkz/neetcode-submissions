class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = ["+","-","*","/"]
        stack = []

        for num in tokens:
            if num in operations:
                right = stack.pop()
                left = stack.pop()
                if num == "+":
                    stack.append(left + right)
                elif num == "-":
                    stack.append(left - right)
                elif num == "*":
                    stack.append(left * right)
                elif num == "/":
                    stack.append(int(left /right))
            else:
                stack.append(int(num))
        return stack[0]
                    

                    
