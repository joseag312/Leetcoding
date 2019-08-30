# Idea from FFurus:
# Using modulo and lists, I believe an approach like this could be generated with.
# Logic similar to the Plus One problem established before.

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        num1 = list(a)
        num2 = list(b)
        c, d, sum = 0, 0, ''
        while num1 or num2:
            x, y = 0, 0
            if num1:
                x = int(num1.pop())
            if num2:
                y = int(num2.pop())
            c, d = (x + y + c)//2, (x + y + c)%2
            sum = str(d) + sum
        
        if c != 0:
            return str(c) + sum
        else:
            return sum

testcase = ['1']
testcase2 = ['11']
mysol = Solution()  
for i in range(len(testcase)):
    print(mysol.addBinary(testcase[i],testcase2[i]))
    