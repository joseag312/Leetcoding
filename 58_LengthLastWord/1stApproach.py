from typing import List

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        if not s:
            return(0)
        elif ' ' in s:
            s = s[::-1]
            while s[:1] == ' ' and len(s) > 1:
                s = s[1:]
            if s:
                if ' ' in s:
                    return s.index(' ')
                else:
                    return len(s)
            else:
                return 0

        else:
            return len(s)

testcase = '       '
mysol = Solution()  
print(mysol.lengthOfLastWord(testcase))
    