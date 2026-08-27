class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROW, COL = len(matrix), len(matrix[0])
        top, bot = 0, ROW - 1

        while top <= bot:
            """row is the row we are checking"""
            row = (top + bot) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break

        if not (top <= bot):
            return False
        row = (top + bot) // 2
        l , r = 0, COL - 1
        while l <= r:
            m = (l + r) // 2
            if target == matrix[row][m]:
                return True
            
            if target > matrix[row][m]:
                l = m + 1
            else:
                r = m - 1
        return False

