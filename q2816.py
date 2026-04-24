# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def doubleIt(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        number=0
        curr=head
        while curr:
            data=curr.val
            number=number*10+data
            curr=curr.next
        number=number*2
        number=str(number)
        rethead=ListNode(0)
        ans=rethead
        n=len(number)
        for i in range(n):
            d=int(number[i])
            rethead.next=ListNode(d)
            rethead=rethead.next
        return ans.next