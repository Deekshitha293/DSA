public class Solution {
    public boolean hasCycle(ListNode head) {
        if (head == null || head.next == null) {
            return false; // no nodes or only one node → no cycle
        }

        ListNode slow = head;
        ListNode fast = head;

        while (fast != null && fast.next != null) {
            slow = slow.next;        // move by 1 step
            fast = fast.next.next;   // move by 2 steps

            if (slow == fast) {
                return true; // cycle found
            }
        }

        return false; // fast reached null → no cycle
    }
}
