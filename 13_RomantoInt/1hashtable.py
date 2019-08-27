from typing import List

class Solution:
    def romanToInt(self, s: str) -> int:
          
        '''
        I             1
        V             5
        X             10
        L             50
        C             100
        D             500
        M             1000
        '''
        
        my_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        my_int = 0
        oldbuffer = 1001

        for i in range(len(s)):
            buffer = my_dict[s[i]]
            if buffer > oldbuffer:
                my_int += buffer - 2*oldbuffer
            else:
                my_int += buffer
            oldbuffer = buffer


        return(my_int)

testcase = ['I', 'XX', 'IV', 'XXXIII','D', 'XIII', 'CCCX', 'CDLXXXIX', 'MCMLII', 'MCMXCIV', 'MMMCMXCIX']
mysol = Solution()  
for i in range(len(testcase)):
    print(mysol.romanToInt(testcase[i]))
