# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        nodes_seen = {0}
        curr = head
        while curr != None:
            if curr.next in nodes_seen:
                return True
            else:
                nodes_seen.add(curr.next)
            curr = curr.next
        return False

        