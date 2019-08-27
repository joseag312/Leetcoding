# Why the need for so many variables? This approach just checks if
# the first letter matches, and checks for all the following letters
# if the j for loops exits naturally, this means all the letters
# match and thus, the program returns the index naturally.

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        len_needle = len(needle)
        len_haystack = len(haystack)

        if len_needle == 0:
            return(0)

        for i in range(len_haystack):
            if (i + len_needle) > len_haystack:
                break
            elif needle[0] == haystack[i]:
                for j in range(1, len_needle):
                    if needle[j] != haystack[i+j]:
                        break
                else:
                    return(i)

        return(-1)

#              1        2       3         4       5    6    7       8
testcase = ['hello', 'Great', 'great', 'aaaaa', 'aaa', '', 'a', 'mississippi']
#             1     2     3     4     5     6   7       8
testcase2 = ['ll', 'gr', 'gr', 'b', 'aaa', 'a', '', 'issip'] 
mysol = Solution()  
for i in range(len(testcase)):
    print(mysol.strStr(testcase[i], testcase2[i]))
    

    