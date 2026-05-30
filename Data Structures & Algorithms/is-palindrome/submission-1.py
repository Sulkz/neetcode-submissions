class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s = s.lower().replace(" ", "")
        n = ""
        

        for char in s:
            if char.isalnum():
                n += char

        l, r = 0 , len(n) - 1


        while l < r:
            if n[l] != n[r]:
                return False
            l += 1
            r -= 1
        return True
            

