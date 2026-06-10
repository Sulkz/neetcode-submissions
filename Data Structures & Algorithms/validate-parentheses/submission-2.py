class Solution:
    def isValid(self, s: str) -> bool:
        isValid = {")":"(", "}":"{", "]":"["}
        check = []

        for sym in s:
            if sym in isValid:
                if check and check[-1] == isValid[sym]:
                    check.pop()
                else:
                    return False
            else:
                check.append(sym) 
        return True if not check else False       