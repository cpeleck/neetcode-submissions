# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None or head.next == None or head.next.next == None:
            return False

        s, f = head, head
        s = s.next
        f = f.next.next
        while s != f:
            try:
                s = s.next
                f = f.next.next
            except:
                return False
        return f != None
        
        

        