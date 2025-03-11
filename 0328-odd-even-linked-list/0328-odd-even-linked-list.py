# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        start_of_odd = odd = head
        start_of_even = even = head.next
        while odd.next and odd.next.next:
            odd.next = odd.next.next
            odd = odd.next
            if even.next and even.next.next:
                even.next = even.next.next
                even = even.next
        odd.next = start_of_even
        even.next = None
        return start_of_odd
        