'''
input integer array - nums
process- if any value appears more True than once in the array else false
output - bool 
'''
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        no_duplicates = set(nums)
        if len(no_duplicates) != len(nums):
            return True
        return False
        