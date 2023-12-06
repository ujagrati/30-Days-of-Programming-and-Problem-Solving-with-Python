# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        vnodes = set()
        curr = head
        while curr:
            if curr in vnodes:
                return True
            vnodes.add(curr)
            curr= curr.next
        return False

        