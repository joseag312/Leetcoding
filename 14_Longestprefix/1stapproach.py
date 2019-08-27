strs = ["flower","flow","flight", "fl", ""]
minw = min(strs, key = len) #fl


for i in range(len(minw)+1):
    check = minw[:i]
    for j, w in enumerate(strs):
        if w[:i] != check:
            print(check[:i-1])
            break
else:
    print(minw)