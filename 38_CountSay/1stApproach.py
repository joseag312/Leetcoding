# In this approach I used the buffer concept from Ex 9

class Solution:
    def countAndSay(self, n: int) -> str:

        if n == 1:
            return '1'

        previous = '1'

        for i in range(1, n):
            
            current = ''
            buf = previous[:1]
            count = 1
            for c in previous[1:]:
                if c == buf: 
                    count += 1
                else:
                    current += str(count) + str(buf)
                    buf = c
                    count = 1
            
            current += str(count) + str(buf)
            previous = current

        return(previous)

testcase = [14]
mysol = Solution()  
for i in range(len(testcase)):
    print(mysol.countAndSay(testcase[i]))
    