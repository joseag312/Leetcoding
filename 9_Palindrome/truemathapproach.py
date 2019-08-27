x = 1
checker = 0

if x < 0 or (x % 10 == 0 and x != 0):
    print (False)

while x > checker:
    checker = checker * 10 + (x % 10)
    x = x // 10

print(x == checker or x == checker // 10)
