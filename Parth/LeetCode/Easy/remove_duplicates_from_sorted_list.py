"""
Runtime: 44 ms
Memory: 13.6 MB
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    """
    Problem Statement:
    Given a sorted linked list, delete all duplicates such that each element appear only once.

    Input: 1 -> 1 -> 2
    Output: 1 -> 2
    """

    def deleteDuplicates(self, head: ListNode) -> ListNode:

        if head == None:
            return head
        
        current = head.next
        prev = head
        
        while current != None:
            if current.val == prev.val:
                prev.next = current.next
                current = current.next
            else:
                current = current.next
                prev = prev.next
        
        return head
