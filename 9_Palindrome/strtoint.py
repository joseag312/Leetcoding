x = -12321
x = str(x)
leng = len(x)
hleng = (len(x)//2)
left = x[0:1]
right = x[leng - 1: leng -2 : -1]
print(hleng)
for i in range(hleng):
    left = x[i:i+1]
    right = x[leng - i -1:leng - i - 2:-1]
    if left != right:
        print (False)

print (True)