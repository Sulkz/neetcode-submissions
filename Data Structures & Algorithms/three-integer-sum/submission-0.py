class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []

        if not nums:
            return []

        for m in range(len(nums) - 2):
            if m > 0 and nums[m] == nums[m-1]:
                continue
            l, r = m + 1, len(nums) - 1
            while l < r:
                total = nums[m] + nums[l] + nums[r]
                if total > 0:
                    r -= 1
                elif total < 0:
                    l += 1
                else:
                    res.append([nums[m], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1
        return res