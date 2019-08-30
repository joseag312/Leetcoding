from typing import List

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l = 0
        s = s.strip()

        for c in s:
            if c == ' ':
                l = 0
            else:
                l += 1

        return(l)

testcase = ' hey       '
mysol = Solution()  
print(mysol.lengthOfLastWord(testcase))
    