# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or not head.next:
            return head
        else:
            cur = head.next
            head.next = None
            prev = head
            
            while cur:
                r_cur = cur.next
                cur.next = prev
                prev = cur
                cur = r_cur
            
            return prev
