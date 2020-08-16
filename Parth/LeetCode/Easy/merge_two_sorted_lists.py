"""
Looked up the solution to understand linked list implementation in Python

Runtime: 40 ms
Memory Usage: 13.7 MB
"""


class ListNode:

    """
    Definition for singly linked list.
    """
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    """
    Problem Statement: 
    Merge two sorted linked lists and return it as a new sorted list. 
    The new list should be made by splicing together the nodes of the first two lists.
    
    Input: 1 -> 2 -> 4, 1 -> 3 -> 4
    Output: 1 -> 1 -> 2 -> 3 -> 4 -> 4
    """

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        dummy = temp = ListNode(0)

        while l1 != None and l2 != None:

            if l1.val < l2.val:
                temp.next = l1
                l1 = l1.next
            else:
                temp.next = l2
                l2 = l2.next
            temp = temp.next

        temp.next = l1 or l2

        return dummy.next