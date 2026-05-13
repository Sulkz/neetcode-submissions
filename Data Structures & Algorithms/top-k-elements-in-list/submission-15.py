class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        results = []
        count = {}

        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 0
        
        count = sorted(count.items(), key=lambda x: x[1], reverse=True)

        for key, _ in count:
            results.append(key)
        return results[:k]
        
        