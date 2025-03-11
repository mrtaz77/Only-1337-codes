# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        move_slow = False
        if fast.next is None:
            head = head.next
        while fast.next is not None:
            fast = fast.next
            if fast.next is not None:
                if move_slow:
                    slow = slow.next
                move_slow = ~move_slow
            else:
                temp = slow.next
                slow.next = slow.next.next
                temp.next = None
        return head

            
            
        