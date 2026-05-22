from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        count = Counter(nums)
        order = sorted(count.items(), key= lambda x: x[1], reverse=True)
        
        for key, _  in order:
            result.append(key)
        return result[:k]

        