class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = sorted(list(s))
        t = sorted(list(t))

        r, l = 0, 0
        if len(s) != len(t):
            return False
        
        while r < len(s) and l < len(t):
            if s[r] == t[l]:
                r += 1
                l += 1
            else:
                return False
        return True 
