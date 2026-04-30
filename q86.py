# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: Optional[ListNode]
        :type x: int
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return head
        curr=head
        less=ListNode(0)
        great=ListNode(0)
        s1=less
        s2=great
        while  curr:
            if curr.val<x:
                less.next=curr
                less=less.next
            else:
                great.next=curr
                great=great.next
            curr=curr.next
        less.next=s2.next
        great.next=None
        return s1.next

        
        
        