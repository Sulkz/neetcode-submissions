class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        new_nums = sorted(set(nums))
        counter = 1
        max_counter = 1
        if not new_nums:
            return 0

        for i in range(1,len(new_nums)):
            if new_nums[i-1] + 1 == new_nums[i]:
                counter += 1
                max_counter = max(max_counter,counter)
            else:
                counter = 1
            
            
        return max_counter