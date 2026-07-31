# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None:
            return list2
        elif list2 == None:
            return list1
        # check head
        if list1.val <= list2.val:
            head = list1 # 1
            curr = list2 # 1
        else:
            head = list2
            curr = list1
        curr1 = head.next # 2
        return_head = head
            
        
        # compare for n + m length
        while curr != None or curr1 != None:
            if curr == None:
                while curr1 != None:
                    head.next = curr1
                    curr1 = curr1.next
                    head = head.next

                break
            elif curr1 == None:
                while curr != None:
                    head.next = curr
                    curr = curr.next
                    head = head.next
                break
            if curr.val <= curr1.val:
                head.next = curr
                curr = curr.next
            else:
                head.next = curr1
                curr1 = curr1.next
            head = head.next
        
        return return_head

        
        



        