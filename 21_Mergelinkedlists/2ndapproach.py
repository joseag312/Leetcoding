class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

l1 = ListNode(1)
l2 = ListNode(2)
l1.next = l2

l3 = ListNode(None)
head = l3

print(l3)
print(head)
print('\n')

l3.next = l1
l1 = l1.next
l3 = l3.next

print(l3)
print(head)

print('\n')
print(l1)
print(l2)

print(l1)