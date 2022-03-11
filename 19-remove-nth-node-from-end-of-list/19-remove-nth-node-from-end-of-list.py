# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head
        c = 0
        while temp:     #Find the length of the linked list
            c+=1
            temp = temp.next
        a = c-n+1       #Calculate the node to be removed
        i = 1
        temp2 = head
        prev = None
        while i < a:         #Traverse till the node to be removed
            i+=1
            prev = temp2     #Prev pointer to point the previous node of the deletion node
            temp2 = temp2.next
        if temp2==head:
            return head.next
        prev.next = temp2.next    #Link the previous node to the next of the deletion node
        return head
            
        
            
        
        