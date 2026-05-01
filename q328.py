# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        curr=head
        odd=ListNode(0)
        even=ListNode(0)
        s1=odd
        s2=even
        while curr:
            odd.next=curr
            odd=odd.next
            even.next=odd.next
            even=even.next
            curr=even.next if (even and even.next ) else None
            
        odd.next=s2.next

        return s1.next
                

            


            