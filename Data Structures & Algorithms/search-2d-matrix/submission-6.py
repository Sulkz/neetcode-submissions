class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for arr in matrix:
            l , r = 0, len(arr) - 1
            flag = False
            while l <= r:
                mid = (l + r) //2
                if arr[mid] == target:
                    flag = True
                    break
                elif target > arr[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
            if flag:
                return True
        return False
        
