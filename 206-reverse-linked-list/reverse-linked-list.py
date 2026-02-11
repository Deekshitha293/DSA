# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        prev = None
        current = head
        
        while current is not None:
            # Store the next node
            next_node = current.next
            
            # Reverse the pointer
            current.next = prev
            
            # Move prev and current one step forward
            prev = current
            current = next_node
        
        # prev is the new head of the reversed list
        return prev
