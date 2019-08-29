# Time limit exceeds in this approach, after changing the storing values to array
# and then looking throught them to a max result, still exceeds time limit.

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        leng = len(nums)
        max_res = -2147483648

        if leng == 1:
            return(nums[0])
        
        for i in range(leng):
            for j in range(i+1, leng+1):
                if sum(nums[i:j]) > max_res:
                    max_res = sum(nums[i:j])
                
        return(max_res)

testcase = [[-2,1,-3,4,-1,2,1,-5,4]]
mysol = Solution()
for i in range(len(testcase)):
    print(mysol.maxSubArray(testcase[i]))
    