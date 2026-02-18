# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        if not head or not head.next:
            return True  # single node or empty list is palindrome
        
        # Step 1: Find the middle using slow & fast pointers
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Step 2: Reverse the second half
        prev = None
        curr = slow
        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp
        
        # Step 3: Compare first half and reversed second half
        first = head
        second = prev  # head of reversed second half
        while second:  # only need to traverse second half
            if first.val != second.val:
                return False
            first = first.next
            second = second.next
        
        # Optional Step 4: Restore the second half if needed (not required by problem)
        
        return True
