x = -9463847412
if x >= 0:
    positive = True
else:
    positive = False

x = int(str(abs(x))[::-1])

if positive:
    if x > (2**31 - 1):
        print(0)
    else:
        print(x)
else:
    x = -x
    if x < -(2**31):
        print(0)
    else:
        print(x)