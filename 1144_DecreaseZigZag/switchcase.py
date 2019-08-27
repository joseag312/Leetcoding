from typing import List
class Solution:
    @staticmethod
    def movesToMakeZigzag(nums: List[int]) -> int:
        moves = [0,0]

        for i in range(0,len(nums),2):
            if i == 0:
                moves[0] += max(0, nums[i] - nums[i+1] + 1)
            elif i == len(nums)-1:
                moves[0] += max(0, nums[i] - nums[i-1] + 1)
            else:
                moves[0] += max(0, nums[i] - min(nums[i+1], nums[i-1]) + 1)

        for i in range(1, len(nums), 2):
            if i == len(nums)-1:
                moves[1] += max(0, nums[i] - nums[i-1] + 1)
            else:
                moves[1] += max(0, nums[i] - min(nums[i+1], nums[i-1]) + 1)
        return min(moves)

data = [[1,2,3]]
for i in range(len(data)):
    print(Solution.movesToMakeZigzag(data[i]))