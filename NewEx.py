from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        leng = len(nums) - 1
        while i <  leng:
            
            if nums[i] == 0:
                j = i + 1
                while j < (leng + 1):
                    if nums[j] != 0:
                        nums[i], nums[j] = nums[j], nums[i]
                        break
                    j += 1
                    
            i += 1


testcase = [0,1,0,3,12]
mysol = Solution()  
for i in testcase:
    print(mysol.moveZeroes(testcase))
    