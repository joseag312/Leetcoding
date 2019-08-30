from typing import List

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l = 0
        s = s[::-1].strip()

        for c in s:
            if c == " ":
                break
            else:
                l += 1

        return(l)

testcase = 'a  '
mysol = Solution()  
print(mysol.lengthOfLastWord(testcase))
    