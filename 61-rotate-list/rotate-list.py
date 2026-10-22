# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head, k):
        if not head or not head.next or k == 0:
            return head

        l = 1
        tail = head

        while tail.next:
            tail = tail.next
            l += 1

        k = k%l
        if k == 0:
            return head

        p = head
        q = head

        for i in range(k):
            q = q.next

        while q.next:
            p = p.next
            q = q.next

        new_head = p.next
        p.next = None
        q.next = head

        return new_head
        