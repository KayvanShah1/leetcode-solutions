# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


from queue import PriorityQueue
# https://stackoverflow.com/questions/40205223/priority-queue-with-tuples-and-dicts


class use_only_first:
    def __init__(self, first, second):
        self._first, self._second = first, second

    def __lt__(self, other):
        return self._first < other._first

    
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        q = PriorityQueue()
        
        for l in lists:
            if l:
                q.put(use_only_first(l.val, l))
                
        head = point = ListNode(0)
        
        # PriorityQueue has no len()
        while not q.empty():
            use_object = q.get()
            val = use_object._first
            node = use_object._second
            point.next = ListNode(val)
            point = point.next
            node = node.next
            
            if node:
                q.put(use_only_first(node.val, node))
                
        return head.next