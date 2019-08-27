from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {}

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in my_dict and my_dict[complement] != i:
                return sorted([i, nums.index(complement)])
            else:
                my_dict[nums[i]] = i
            
        return([-1,-1])

testcase = {'15': [2, 5, 8, 13], '13': [8, 5, 9, 14], '6': [3, 3]}
mysol = Solution()  
for i in testcase:
    print(mysol.twoSum(testcase[i], int(i)))
    