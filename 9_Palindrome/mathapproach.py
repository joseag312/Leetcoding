from math import log10
checker = 0

if x < 0 or (x % 10 == 0 and x != 0):
    print (False)
elif x == 0:
    print (True)
elif (int(log10(x)) + 1) == 1:
    print (True)
else:
    digits = int(log10(x)) + 1

    while (int(log10(x)) + 1) > (digits // 2):
        buf = x % 10
        x = x // 10
        checker = checker * 10 + buf

    if (digits % 2) == 1:
        checker = checker // 10

    if x == checker:
        print (True)
    else:
        print (False)
