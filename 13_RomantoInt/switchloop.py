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
        
        my_int = 0

        
        while s:
            l = len(s)
            if s[-1] == 'M':
                if len(s) > 1:
                    if s[-2] == 'C':
                        my_int += 900
                        s = s[:l-2]
                    else:
                        my_int += 1000
                        s = s[:l-1]
                else:
                    my_int += 1000
                    s = s[:l-1]
            elif s[-1] == 'D':
                if len(s) > 1:
                    if s[-2] == 'C':
                        my_int += 400
                        s = s[:l-2]
                    else:
                        my_int += 500
                        s = s[:l-1]
                else:
                    my_int += 500
                    s = s[:l-1]
            elif s[-1] == 'C':
                if len(s) > 1:
                    if s[-2] == 'X':
                        my_int += 90
                        s = s[:l-2]
                    else:
                        my_int += 100
                        s = s[:l-1]
                else:
                    my_int += 100
                    s = s[:l-1]
            elif s[-1] == 'L':
                if len(s) > 1:
                    if s[-2] == 'X':
                        my_int += 40
                        s = s[:l-2]
                    else:
                        my_int += 50
                        s = s[:l-1]
                else:
                    my_int += 50
                    s = s[:l-1]
            elif s[-1] == 'X':
                if len(s) > 1:
                    if s[-2] == 'I':
                        my_int += 9
                        s = s[:l-2]
                    else:
                        my_int += 10
                        s = s[:l-1]
                else:
                    my_int += 10
                    s = s[:l-1]
            elif s[-1] == 'V':
                if len(s) > 1:
                    if s[-2] == 'I':
                        my_int += 4
                        s = s[:l-2]
                    else:
                        my_int += 5
                        s = s[:l-1]
                else:
                    my_int += 5
                    s = s[:l-1]
            elif s[-1] == 'I':
                my_int += 1
                s = s[:l-1]
            else:
                print('Not a valid number, please input a number between 1 and 3999.')
        

        return(my_int)

testcase = ['I', 'XX', 'IV', 'XXXIII','D', 'XIII', 'CCCX', 'CDLXXXIX', 'MCMLII', 'MCMXCIV', 'MMMCMXCIX']
mysol = Solution()  
for i in range(len(testcase)):
    print(mysol.romanToInt(testcase[i]))
