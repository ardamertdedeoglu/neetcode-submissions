# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1, curr2 = list1, list2
        new_list = ListNode()
        new_list_head = new_list

        while curr1 != None and curr2 != None:
            if curr1.val <= curr2.val:
                new_list.next = curr1
                new_list = new_list.next
                curr1 = curr1.next
            else:
                new_list.next = curr2
                new_list = new_list.next
                curr2 = curr2.next
        
        if curr1 != None:
            while curr1 != None:
                new_list.next = curr1
                new_list = new_list.next
                curr1 = curr1.next
        elif curr2 != None:
            while curr2 != None:
                new_list.next = curr2
                new_list = new_list.next
                curr2 = curr2.next

        return new_list_head.next