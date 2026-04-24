# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: Optional[ListNode]
        :type left: int
        :type right: int
        :rtype: Optional[ListNode]
        """

       
        if not head or left==right:
            return head
        dummy=ListNode(0,head)
        curr=dummy
        count=0
        start=None
        while count<left:
            start=curr
            curr=curr.next
            count+=1
        temp=curr
        finish=curr
        prev=None
        front=None
        while count<=right:
            front=temp.next
            temp.next=prev
            prev=temp
            temp=front
            count+=1
        start.next=prev
        finish.next=front
        return dummy.next

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: Optional[ListNode]
        :type left: int
        :type right: int
        :rtype: Optional[ListNode]
        """

       
        if not head or left==right:
            return head
        dummy=ListNode(0,head)
        prev = dummy

        for _ in range(left - 1):
            prev = prev.next
        
        curr=prev.next
        for _ in range(right-left):
            nextnode=curr.next
            curr.next=nextnode.next
            nextnode.next=prev.next
            prev.next=nextnode
        
        return dummy.next
           
        
        






























        
   
               
            
            