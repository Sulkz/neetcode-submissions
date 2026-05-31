class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(set(nums))
        c, max_c = 1, 1

        if not nums:
            return 0

        for i in range(1, len(nums)):
            if nums[i-1] + 1 == nums[i]:
                c += 1
                max_c = max(max_c,c)
            else:
                c = 1
        return max_c