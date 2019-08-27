nums = [0,0,1,1,1,2,2,3,3,4]
leng = len(nums)


for i in range(len(nums)-1):
    if i == leng:
        break
    while nums[i] == nums[i+1]:
        for j in range(i, len(nums)-1):
            nums[j], nums[j+1] = nums[j+1], nums[j]
        leng += -1
        if i == (leng - 1):
            break
        

print(nums[:leng])