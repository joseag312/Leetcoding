# Understanding the principle from the second approach, this approach just registers the value
# in a variable instead of an array, trying to help both space and time complexity.
# ... Kadane's algorithm lol. https://www.geeksforgeeks.org/largest-sum-contiguous-subarray/

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        if nums == []:
            return -2**31 

        buf = nums[0]
        max_sum = buf
        for i in range(1,len(nums)):
            buf = max(buf + nums[i], nums[i])
            if buf > max_sum:
                max_sum = buf
        if buf < 0:
            buf = 0
        return max_sum

testcase = [[-2,1,-3,4,-1,2,1,-5,4]]
mysol = Solution()
for i in range(len(testcase)):
    print(mysol.maxSubArray(testcase[i]))