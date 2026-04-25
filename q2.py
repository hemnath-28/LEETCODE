# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        curr1=l1
        curr2=l2
        carry=0
        start=ListNode(0)
        ret=start
        while curr1 or curr2 or carry!=0:
            if not curr1:
                val1=0
            else:
                val1=curr1.val
                curr1=curr1.next
            if not curr2:
                val2=0
            else:
                val2=curr2.val
                curr2=curr2.next
                
            data=val1+val2+carry
            carry=data//10
            data=data%10
            start.next=ListNode(data)
            start=start.next
            
            
           
           
        
        return ret.next

            
