# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """
        curr=head
        stack=[]
        length=0
        while curr:
            stack.append(curr)
            curr=curr.next
            length+=1
        length=length//2
        curr=head
        while length>0:
            last=stack.pop()
            front=curr.next
            curr.next=last
            last.next=front
            curr=front
            length-=1
           
        if curr:
            curr.next=None
        return head
            
            