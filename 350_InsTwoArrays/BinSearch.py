from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ins = []
        occ1 = {}
        occ2 = {}

        nums1d = dict.fromkeys(nums1)
        nums2d = dict.fromkeys(nums2)

        for i in range(len(nums2)):
            if nums2[i] in nums1d:
                if nums2[i] in occ1:
                    occ1[nums2[i]] += 1
                else:
                    occ1[nums2[i]] = 1

        for i in range(len(nums1)):
            if nums1[i] in nums2d:
                if nums1[i] in occ2:
                    occ2[nums1[i]] += 1
                else:
                    occ2[nums1[i]] = 1
        
        for key in occ1:
            if occ1[key] < occ2[key]:
                for i in range(occ1[key]):
                    ins.append(key)
            else:
                for i in range(occ2[key]):
                    ins.append(key)
        
        
        return ins


testcase = [[4,9,5],[9,4,9,8,4]]
mysol = Solution()  
print(mysol.intersect(testcase[0], testcase[1]))
    