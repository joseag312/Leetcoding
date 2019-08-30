# 72.54 Python approach using arithmetic and string slicing.
# ...Still improving :)

class Solution:

    def addBinary(self, a: str, b: str) -> str:
        a = a[::-1]
        b = b[::-1]
        lena, lenb = len(a),len(b)
        maxl = max(lena,lenb)
        my_list = [0]*maxl

        for c in range(maxl):
            if c < lena:
                my_list[c] += int(a[c])
            if c < lenb:
                my_list[c] += int(b[c])
            
            if my_list[c] >= 2:
                if c == maxl -1:
                    my_list.append(1)
                    my_list[c] += -2
                else:
                    my_list[c] += -2
                    my_list[c+1] += 1

        my_list.reverse()
        res = ''.join(map(str,my_list))

        return (res)

testcase = ['1111']
testcase2 = ['1111']
mysol = Solution()  
for i in range(len(testcase)):
    print(mysol.addBinary(testcase[i],testcase2[i]))
    