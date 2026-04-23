# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        curr=head
        flag=False
        while curr:
            temp=curr
            while temp.next and curr.val==temp.next.val:
                flag=True
                temp=temp.next
            if flag:
                curr.next=temp.next
                flag=False
            curr=curr.next
        return head
                    
