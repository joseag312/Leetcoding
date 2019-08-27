class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

counter1 ,counter2 = ListNode()
head = ListNode(None)
l3 = ListNode(None)
head.next = l3

while counter1 and counter2:
    if(counter1.val < counter2.val):
        l3.next = counter1
        counter1 = counter1.next
        l3 = l3.next
    else:
        l3.next = counter2
        counter2 = counter2.next
        l3 = l3.next
l3.next = counter1 or counter2
print (head.next.next)