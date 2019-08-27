from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Solving with standard sum isn't working, in order to evaluate most cases, what you need
        # is a recursive function to evaluate all cases:
        # f[i] = cost[i] min(f[i+1], f[i+2])

        price = 0

        def my_recursion(cost, i):
            if len(cost) > (i+2):
                price = cost[i] + min(my_recursion(cost, (i+1)), my_recursion(cost, (i+2)))
            else:
                price = cost[i]
            return price

        return min(my_recursion(cost, 0),my_recursion(cost, 1))

testcase = [[0, 1, 2, 2],[0, 1, 2, 2, 0, 1, 2, 2],[1, 100, 1, 1, 1, 100, 1, 1, 100, 1], [1, 100, 100, 1, 1]]
mysol = Solution()  
for i in range(len(testcase)):
    print(mysol.minCostClimbingStairs(testcase[i]))
