# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        # Orginal List
        if not head:
            return True
        newhead=ListNode(head.val)
        check=newhead
        oldhead=head.next
        while oldhead:
            newhead.next=ListNode(oldhead.val)
            newhead=newhead.next
            oldhead=oldhead.next
        

        # Reverse List

        front=None
        prev=None
        temp=head
        while temp:
            front=temp.next
            temp.next=prev
            prev=temp
            temp=front
        while prev:
            if prev.val!=check.val:
                return False
            prev=prev.next
            check=check.next
        
    
        return True