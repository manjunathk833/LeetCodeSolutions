# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow


'''
Approach 1: Output to Array
Intuition and Algorithm

Put every node into an array A in order. Then the middle node is just A[A.length // 2], since we can retrieve each node by index.

We can initialize the array to be of length 100, as we're told in the problem description that the input contains between 1 and 100 nodes.


Complexity Analysis

Time Complexity: O(N)O(N), where NN is the number of nodes in the given list.

Space Complexity: O(N)O(N), the space used by A.


Approach 2: Fast and Slow Pointer
Intuition and Algorithm

When traversing the list with a pointer slow, make another pointer fast that traverses twice as fast. When fast reaches the end of the list, slow must be in the middle.


Complexity Analysis

Time Complexity: O(N)O(N), where NN is the number of nodes in the given list.

Space Complexity: O(1)O(1), the space used by slow and fast.


'''