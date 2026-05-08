class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        checklist = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in checklist:
                return [checklist[complement], i ]
            checklist[nums[i]] =  i


