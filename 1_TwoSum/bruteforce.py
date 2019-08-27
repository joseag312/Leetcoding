from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if target == (nums[i] + nums[j]):
                    return([i,j])
        return([-1,-1])


testcase = {'15': [2, 5, 8, 13], '13': [8, 5, 9, 14], '6': [3, 3]}
mysol = Solution()
for i in testcase:
    print(mysol.twoSum(testcase[i], int(i)))
    