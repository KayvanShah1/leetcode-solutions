# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum_head = ListNode()

        carry = 0
        curr_sum = sum_head

        while l1 or l2 or carry:
            if l1:
                l1_val = l1.val
                l1 = l1.next
            else:
                l1_val = 0

            if l2:
                l2_val = l2.val
                l2 = l2.next
            else:
                l2_val = 0

            carry, sum_ = divmod(l1_val + l2_val + carry, 10) 
            curr_sum.next = ListNode(sum_)
            curr_sum = curr_sum.next

        return sum_head.next
