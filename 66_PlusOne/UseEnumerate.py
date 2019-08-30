from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        buf = 0
        for d in digits:
            buf = buf*10 + d
        buf += 1

        return(list(map(int,str(buf))))

testcase = [[9,9,9]]
mysol = Solution()  
for i in range(len(testcase)):
    print(mysol.plusOne(testcase[i]))