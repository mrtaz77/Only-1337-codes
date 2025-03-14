# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or head.next is None:
            return head
        new_head = self.reverseList(head.next)
        itr = new_head
        while itr.next is not None:
            itr = itr.next
        itr.next = head
        head.next = None
        return new_head
        