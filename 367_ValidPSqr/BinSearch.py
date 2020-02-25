class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        low = 0
        high = num
        res = num//2

        if num == 0:
            return False
        if num == 1:
            return True
        
        while (num/res) != res and low < high:
            
            if (num//res) > res:
                low = res + 1
                res = low + (high - low)//2
            else:
                high = res
                res = low + (high - low)//2
        else:
            if num/res == res:
                return True
        
        return False


testcase = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
mysol = Solution() 
for i in range(len(testcase)):
    print(mysol.isPerfectSquare(testcase[i]))
    