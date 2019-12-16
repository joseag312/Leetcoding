class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        
        if head == None or head.next == None:
            return head
        
        equisita = self.reverseList(head.next) 
        head.next.next = head
        head.next = None
        return equisita

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
print(mysol.reverseList(n1))
    