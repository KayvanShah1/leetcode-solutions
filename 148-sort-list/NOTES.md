# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
​
​
class Solution:
tail = ListNode()
nextSubList = ListNode()
def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
if head is None or head.next is None:
return head
n = self.getCount(head)
start = head
dummyHead = ListNode()
for i in range(1,n,2):
tail = dummyHead
while start is not None:
if start.next is None:
break
return dummyHead.next
def getCount(self, head):
count = 0
pointer = ListNode()
while pointer is not None:
pointer = pointer.next
count += 1
​
return count