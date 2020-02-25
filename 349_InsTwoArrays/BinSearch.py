from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        ins = []
        
        if len(nums1) <= len(nums2):
            
            if not nums1:
                return ins
            
            nums1 = list(dict.fromkeys(sorted(nums1)))
            
            for i in range(len(nums2)):
                
                low = 0
                high  = len(nums1) - 1
                index = high // 2
                target = nums2[i]
                
                if not nums1:
                    return ins
                
                while target != nums1[index]:
                    if target > nums1[index]:
                        low = index + 1 
                        index = low + (high - low)//2
                    elif target < nums1[index]:
                        high = index
                        index = low + (high - low)//2
                    if low >= high:
                        if target == nums1[index]:
                            ins.append(target)
                        break
                else:
                    ins.append(target)
                
            
        else:
            
            if not nums2:
                return ins
            
            nums2 = list(dict.fromkeys(sorted(nums2)))
            
            for i in range(len(nums1)):
                
                low = 0
                high  = len(nums2) - 1
                index = high // 2
                target = nums1[i]
                
                while target != nums2[index]:
                    if target > nums2[index]:
                        low = index + 1 
                        index = low + (high - low)//2
                    elif target < nums2[index]:
                        high = index
                        index = low + (high - low)//2
                    if low >= high:
                        if target == nums2[index]:
                            ins.append(target)
                        break
                else:
                    ins.append(target)
            
        return list(dict.fromkeys(ins))


testcase = [[1],[2,3]]
mysol = Solution()  
listprint(mysol.intersection(testcase[0], testcase[1]))
    