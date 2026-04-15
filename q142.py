# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# 1st method using hashtable
class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        

        hashtable={}
        curr=head
        
        while curr and curr.next is not None:
            if curr in hashtable:
                return curr
            hashtable[curr]=1
            curr=curr.next
        return None


# Follow on O(1) --Trying


class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if head is None or head.next is None:
            return None
        slow=head
        fast=head
        curr=head

        while fast and fast.next :
            slow=slow.next
            if fast.next.next:
                fast=fast.next.next
            else:
                return None

            if slow==fast:
                break

        while slow!=curr:
            if slow.next:
                slow=slow.next
                curr=curr.next
            else:
                return None
        return curr
