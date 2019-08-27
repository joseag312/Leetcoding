nums = [0,0,1,1,1,2,2,3,3,4]
i = 0

if len(nums) == 0:
    print (0) 

for j in range(len(nums)):
    if nums[i] != nums[j]:
        i += 1
        nums[i], nums[j] = nums[j], nums[i]

print(nums[:i+1])