from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        if digits:
            digits.reverse()
            digits[0] = digits[0] + 1
            for d in range(len(digits)):
                if digits[d] == 10:
                    if d == len(digits) - 1:
                        digits.append(1)
                        digits[d] = 0
                    else:
                        digits[d], digits[d+1] = 0, digits[d+1] + 1
            digits.reverse()
        else:
            digits.append(1)

        return(digits)

testcase = [[9,9,9]]
mysol = Solution()  
for i in range(len(testcase)):
    print(mysol.plusOne(testcase[i]))
    