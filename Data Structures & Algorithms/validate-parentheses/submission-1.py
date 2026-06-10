class Solution:
    def isValid(self, s: str) -> bool:
        res = []
        s = list(s)
        check = {")":"(", "]":"[","}":"{"}

        for char in s:
            if char in check:
                if res and res[-1] == check[char]:
                    res.pop()
                else:
                    return False
            else:
                res.append(char)
        return True if not res else False
        
                
                    