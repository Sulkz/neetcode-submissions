class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for m in range(len(nums)):
            if m > 0 and nums[m-1] == nums[m]:
                continue
            l, r = m + 1, len(nums) -1
            while l < r:
                total = nums[m] + nums[l] + nums[r]
                if total > 0:
                    r -= 1
                elif total < 0:
                    l += 1
                else:
                    result.append([nums[m],nums[l],nums[r]])
                    l += 1
                    while l < r and nums[l-1] == nums[l]:
                        l += 1
        return result