# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
            
        original_list = []
        while head != None:
            original_list.append(head)
            head = head.next
        
        for i in range(len(original_list)):
            curr_node = original_list[i]
            if i == 0:
                curr_node.next = None
            else:
                curr_node.next = original_list[i - 1]
        
        return original_list[-1]
        