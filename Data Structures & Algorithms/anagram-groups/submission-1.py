class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        check = {}

        for word in strs:
            key = ''.join(sorted(word))

            if key not in check:
                check[key] = []
            check[key].append(word)
        return list(check.values())
 

        