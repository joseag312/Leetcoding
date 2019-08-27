from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # With this iterative algorithm, we call on the first and second costs of each number we iterate through

        first, second = cost[0], cost[1]
        for i in range(2, len(cost)):
            first, second = second, min(first, second) + cost[i]
        return min(first, second)

testcase = [[0, 1, 2, 2],[0, 1, 2, 2, 0, 1, 2, 2],[1, 100, 1, 1, 1, 100, 1, 1, 100, 1], [1, 100, 100, 1, 1]]
mysol = Solution()  
for i in range(len(testcase)):
    print(mysol.minCostClimbingStairs(testcase[i]))
