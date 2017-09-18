# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        curr = head
        end = head
        prev_del = head
        i = 1
        while (i<n):
            end = end.next
            i +=1
        while (end.next != None):
            curr=curr.next 
            end = end.next
        if (curr == head):
            return head.next
        while (prev_del.next != curr):
            prev_del = prev_del.next
        prev_del.next = prev_del.next.next
        return head
        
