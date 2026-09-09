# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        # there is a cycle if fast and slow pointers intersect

        fast = head
        slow = head

        if not head:
            return False

        while fast:

            if not slow.next:
                return False
            if not fast.next or not fast.next.next:
                return False
            slow = slow.next
            fast = fast.next.next

            if fast == slow:
                return True
        return False



            