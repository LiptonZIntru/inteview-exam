# Task 5 finished at 22:35 27.6.2020
class Solution: 
    def getRange(self, arr, target):
        solution = [-1, -1]
        got_first = False

        for i in range(len(arr)):
            if arr[i] == target:
                if not got_first:
                    got_first = True
                    solution[0] = i
                solution[1] = i
        return solution
                

  
# Test program 
arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8] 
x = 2
print(Solution().getRange(arr, x))
# [1, 4]