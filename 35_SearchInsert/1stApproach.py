# Faster than 99.71!!!

from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
          
        if nums == []:
            return(0)

        if target <= nums[0]:
            return(0)

        for i in range(1, len(nums)):
            if (target <= nums[i]):
                return i

        return(len(nums))

testcase = [[1,3,5], [1,3], [1,3,5,6], [1,3,5,6], [1,3,5,6], [1,3,5,6]]
testcase2 = [4, 2, 6, 2, 7, 0]
mysol = Solution()  
for i in range(len(testcase)):
    print(mysol.searchInsert(testcase[i], testcase2[i]))
    