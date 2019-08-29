# Idea from zhanweiting
# Holy... this approach used dynamic programming to solve this and it was absolutely
# ridiculous, I guess I understand the principle though.
# As we advance through the elements in the sequence, we assign either the sum of
# the previous numbers or just the present number, thus excluding combinations 
# which yield smaller values.

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0]*len(nums)
        dp[0] = nums[0]
        for i in range(1,len(nums)):
            dp[i] = max(dp[i-1] +nums[i],nums[i])
        return max(dp)

testcase = [[-2,1,-3,4,-1,2,1,-5,4]]
mysol = Solution()
for i in range(len(testcase)):
    print(mysol.maxSubArray(testcase[i]))