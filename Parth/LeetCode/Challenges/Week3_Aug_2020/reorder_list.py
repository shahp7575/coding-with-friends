"""
Linked list to deque to linked list

Runtime: 148 ms
Memory: 23.2 MB
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        temp = head
        
        d = []
        while(temp != None):
            d.append(temp.val)
            temp = temp.next
            
        i = 0
        temp = head
        while(len(d) > 0):
            if i % 2 == 0:
                temp.val = d[0]
                d.pop(0)
            else:
                temp.val = d[-1]
                d.pop()
            i = i + 1
            
            temp = temp.next
        
        return head
                