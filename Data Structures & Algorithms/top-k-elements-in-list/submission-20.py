class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        res = []
      
        count = Counter(nums)
        counts = sorted(count.items(), key=lambda x : x[1], reverse=True)

        for key, _ in counts:
            res.append(key)
        return res[:k]