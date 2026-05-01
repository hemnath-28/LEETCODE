# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        curr1=list1
        curr2=list2
        ret=ListNode(0)
        dummy=ret
        while curr1 or curr2:
    
            data2=curr2.val if curr2 else 1000
            while curr1 and curr1.val<=data2:
                ret.next=curr1
                ret=ret.next
                curr1=curr1.next
            data1=curr1.val if curr1 else 1000
            while curr2 and curr2.val<=data1:
                ret.next=curr2
                ret=ret.next
                curr2=curr2.next
        return dummy.next



        