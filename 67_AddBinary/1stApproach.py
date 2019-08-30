class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        return bin(int(a, 2) + int(b, 2))[2:]

testcase = ['1']
testcase2 = ['11']
mysol = Solution()  
for i in range(len(testcase)):
    print(mysol.addBinary(testcase[i],testcase2[i]))
    