from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        i = 0
        leng = len(nums)

        while i <  leng:
            if nums[i] == val:
                nums[i],nums[leng-1] = nums[leng-1], nums[i]
                leng += -1
            else:
                i += 1
            
        return(leng)

testcase = [[3,2,2,3], [0,1,2,2,3,0,4,2]]
testcase2 = [3, 2]
mysol = Solution()  
for i in range(len(testcase)):
    print(mysol.removeElement(testcase[i], testcase2[i]))
    