# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return head
        length=0
        l=head
        curr=head
        while l.next:
            l=l.next
            length+=1
        length=length+1
        k=k%length
        l.next=head
        rem=length-k
        for _ in range(rem-1):
            curr=curr.next
        ret=curr.next
        curr.next=None
    
        return ret