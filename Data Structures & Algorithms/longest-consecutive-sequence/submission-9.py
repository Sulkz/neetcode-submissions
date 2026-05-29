class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        new_num_array = sorted(set(nums))
        counter = 1
        max_counter = 1

        if not nums:
            return 0

        for i in range(1,len(new_num_array)):
            if new_num_array[i - 1] + 1 == new_num_array[i]:
                counter += 1        #1          #4
                max_counter = max(max_counter, counter)
            else:
                counter = 1
        return max_counter

