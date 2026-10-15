# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode | None, x: int) -> ListNode | None:
        small = ListNode()
        big = ListNode()

        p1 = small
        p2 = big

        while head:
            if head.val < x:
                p1.next = head
                p1 = p1.next
            else:
                p2.next = head
                p2 = head
            head = head.next
        
        p2.next = None
        p1.next = big.next

        return small.next
        