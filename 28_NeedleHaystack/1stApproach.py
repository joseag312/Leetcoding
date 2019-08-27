# FAILED:
# When this is attempted the iteration skips one letter, and
# when that letter is the start of the needle again, the program
# returns -1 instead of 4 for mississippi.

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        len_needle = len(needle)
        len_haystack = len(haystack)
        MyIndex = 0
        Pos = 0

        if len_needle == 0:
            return(0)

        for i in range(len_haystack):
            if (i - Pos + len_needle) > len_haystack:
                break
            elif needle[Pos] == haystack[i]:
                MyIndex = i - Pos
                Pos += 1
                if Pos == len_needle:
                    return(MyIndex)
            else:
                Pos = 0

        return(-1)

#              1        2       3         4       5    6    7       8
testcase = ['hello', 'Great', 'great', 'aaaaa', 'aaa', '', 'a', 'mississippi'] #Break on mississippi skips one letter
#             1     2     3     4     5     6   7       8
testcase2 = ['ll', 'gr', 'gr', 'b', 'aaa', 'a', '', 'issip'] 
mysol = Solution()  
for i in range(len(testcase)):
    print(mysol.strStr(testcase[i], testcase2[i]))
    
