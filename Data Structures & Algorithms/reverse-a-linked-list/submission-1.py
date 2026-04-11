# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head:
            return head

        next_node = head.next
        head.next = None
        prev_node = head.next

        while(next_node):
            prev_node = head
            head = next_node
            next_node = head.next

            head.next = prev_node

        return head