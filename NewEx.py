from typing import List

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:



        return([-1,-1])


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

testcase = n1
mysol = Solution()  
for i in testcase:
    print(mysol.name_of_function('Arguments'))
    