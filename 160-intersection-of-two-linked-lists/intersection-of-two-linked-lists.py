# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type headA: ListNode
        :type headB: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        
        pA = headA
        pB = headB
        
        # Traverse both lists; switch head when reaching the end
        while pA != pB:
            pA = pA.next if pA else headB
            pB = pB.next if pB else headA
        
        # Either intersection node or None
        return pA
