from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        ins = []
        if len(nums1) <= len(nums2):
            nums1 = dict.fromkeys(nums1)

            for i in range(len(nums2)):
                if nums2[i] in nums1:
                    ins.append(nums2[i])

        else:
            nums2 = dict.fromkeys(nums2)
            for i in range(len(nums1)):
                if nums1[i] in nums2:
                    ins.append(nums1[i])
        
        return ins


testcase = [[1],[2,3]]
mysol = Solution()  
print(mysol.intersection(testcase[0], testcase[1]))
    