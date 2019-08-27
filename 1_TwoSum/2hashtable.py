from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {nums[i] : i for i in range(len(nums))}

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in nums and my_dict.get(complement) != i:
                return[i, my_dict.get(complement)]
        return([-1,-1])

testcase = {'15': [2, 5, 8, 13], '13': [8, 5, 9, 14], '6': [3, 3]}
mysol = Solution()  
for i in testcase: 
    print(mysol.twoSum(testcase[i], int(i)))
