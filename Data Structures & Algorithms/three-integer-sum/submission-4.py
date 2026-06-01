class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []

        if not nums:
            return []

        for m in range(len(nums)):
            if m > 0 and nums[m-1] == nums[m]:
                continue
            l, r = m+1, len(nums)-1
            while l < r:
                total = nums[m] + nums[l] + nums[r]
                if total < 0:
                    l += 1
                elif total > 0:
                    r -= 1
                else:
                    res.append([nums[m], nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l-1] == nums[l]:
                        l += 1
        return res
