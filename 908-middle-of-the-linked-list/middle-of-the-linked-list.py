# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Step 1: Count the number of nodes
        count = 0
        temp = head
        while temp:
            count += 1
            temp = temp.next

        # Step 2: Find the middle index
        middle_index = count // 2

        # Step 3: Move to the middle node
        temp = head
        for _ in range(middle_index):
            temp = temp.next

        # Step 4: Return the middle node
        return temp
