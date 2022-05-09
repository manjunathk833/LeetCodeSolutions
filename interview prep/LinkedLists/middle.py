# https://leetcode.com/problems/middle-of-the-linked-list/submissions/
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        first = sec = head

        while first:
            if first.next == None:
                return sec
            if first.next.next == None:
                return sec.next
            sec = sec.next
            first = first.next.next