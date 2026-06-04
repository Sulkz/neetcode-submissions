class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for i in range(len(strs)):
            ana = ''.join(sorted(strs[i]))
            res[ana].append(strs[i])
        return list(res.values())
