class Solution:
    def maxArea(self, heights: List[int]) -> int:
        '''
        bar has to be the same height or more 
        we will use the two pointer approach
        we want to calc each max amount for each bar
        we have a pointer at the first abr and the last bar 
        if we have to get the min hight of the two b ars then iuse that at times kt byt the distance 

        '''
        water = 0
        max_water = 0 
        l, r = 0, len(heights)-1

        while l < r:
            min_cap = min(heights[l], heights[r])
            dist  = (r - l)
            water = min_cap * dist
            max_water = max(max_water, water)
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return max_water
            


            
