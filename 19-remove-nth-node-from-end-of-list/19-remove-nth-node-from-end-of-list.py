# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = temp2 = head
        
        # Find the length of the linked list
        c = 0
        while temp:     
            c += 1
            temp = temp.next
            
        # Calculate the node to be removed     
        a = c - n + 1 
        
        i = 1
        prev = None
        # Traverse till the node to be removed
        while i < a:         
            i += 1
            # Prev pointer to point the previous node of the deletion node
            prev = temp2     
            temp2 = temp2.next
            
        if temp2 == head:
            return head.next
        
        # Link the previous node to the next of the deletion node
        prev.next = temp2.next 
        return head
            
        
            
        
        