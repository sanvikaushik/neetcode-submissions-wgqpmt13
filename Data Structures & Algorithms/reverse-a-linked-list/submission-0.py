# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        prev = None

        while (head):

            next_node = head.next
            
            if (not prev):
                head.next = None
            else:
                head.next = prev
                
            prev = head
            head = next_node

        return prev


