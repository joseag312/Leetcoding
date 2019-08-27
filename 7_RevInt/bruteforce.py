my_num = 8463847412
rev = 0
if my_num >= 0:
    positive = True
    leng = len(f'{my_num}')
else:
    positive = False
    leng = len(f'{my_num}') - 1

my_num = abs(my_num)
for i in range(leng):
    buf = my_num % 10
    my_num = my_num // 10
    if positive == True:
        if rev + buf/10 > (2147483647/10):
            rev = 0
            break
        else:
            rev = rev*10 + buf
    else:
        if rev + buf/10 > (2147483648/10):
            rev = 0
            break
        else:
            rev = rev*10 + buf

if positive == False:
    rev = -rev

print(rev)