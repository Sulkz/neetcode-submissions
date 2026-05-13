class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        results = []
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        count = sorted(count.items(), key=lambda x: x[1], reverse=True)

        for key, _ in count:
            results.append(key)
        return results[:k]
        
        