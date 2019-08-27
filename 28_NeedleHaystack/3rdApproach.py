# Idea from Billow_jt:
# Why check for each letter? Python has the ability to use slicing in strings.
# NOTE: If you're using slicing please remember last element not inclusive!

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        len_needle = len(needle)
        len_haystack = len(haystack)


        if len_needle == 0:
            return(0)

        if needle == haystack:
            return(0)

        for i in range(len_haystack - len_needle + 1):
            comp = haystack[i:i+len_needle]
            if needle == haystack[i:i + len_needle]:
                return i

        return(-1)
    

#              1        2       3         4       5    6    7       8               9               10
testcase = ['hello', 'Great', 'great', 'aaaaa', 'aaa', '', 'a', 'mississippi', 'mississippi', 'mississippi']
#             1     2     3     4     5     6   7       8      9    10
testcase2 = ['ll', 'gr', 'gr', 'b', 'aaa', 'a', '', 'issip', 'pi', 'ti'] 
mysol = Solution()  
for i in range(len(testcase)):
    print(mysol.strStr(testcase[i], testcase2[i]))
    

    