# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        if not head:
            return 
        if head and not head.next:
            return

        # first find length
        length = 0
        curr = head

        while curr:
            length += 1
            curr = curr.next

        # 1-indexed
        index = length - n + 1

        curr = head
        next_p = None
        prev = None
        i = 1

        while curr:
            if i == index - 1:
                prev = curr
            if i == index + 1:
                next_p = curr

            if i == index:
                delete = curr
            i += 1
            
            curr = curr.next
        
        # now we have set both pointers
        if prev == None:
            return delete.next

        tmp = prev.next
        prev.next = next_p
        tmp.next = None

        return head

