class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if not temperatures:
            return []
        
        res = []

        for i in range(len(temperatures)):
            counter = 1
            j = i + 1
            while j < len(temperatures):
                if temperatures[j] > temperatures[i]:
                    break
                j += 1
                counter +=1
            counter = 0 if j == len(temperatures) else counter
            res.append(counter)
        return res
                




