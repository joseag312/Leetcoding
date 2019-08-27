from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Solving with standard sum isn't working, in order to evaluate most cases, what you need
        # is a recursive function to evaluate all cases:
        # f[i] = min(f[i+1], f[i+2])
        
        # Iterating from front to back evaluates all the posibilities, no need to do so if you evaluate from back to front!
        # Run time exceeds because of recursion principles!
        

        price = 0

        

testcase = [[0, 1, 2, 2],[0, 1, 2, 2, 0, 1, 2, 2],[1, 100, 1, 1, 1, 100, 1, 1, 100, 1], [1, 100, 100, 1, 1]]
mysol = Solution()  
for i in range(len(testcase)):
    print(mysol.minCostClimbingStairs(testcase[i]))
