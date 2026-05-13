from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1:
            return[nums[0]]
        
        if len(nums) == 2:
            if nums[0] != nums[1]:
                return[nums[0],nums[1]]
        
        count = Counter(nums)
        result = []
        for key, val in sorted(count.items(), key=lambda x:x[1],reverse=True):
            result.append(key)
        return result[:k]
        


        

