# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def swapPairs(self, head):
        if not head or not head.next:
            return head

        curr = head
        ret = None
        dummy = ListNode(0)

        while curr:
            first = curr
            snd = curr.next

            # ⚠️ prevent crash when no pair
            if not snd:
                break

            third = snd.next

            dummy.next = snd
            curr = snd
            curr.next = first

            dummy = first
            curr = third

        return dummy.next


# 🔹 Helper function to print linked list
def print_list(head):
    curr = head
    while curr:
        print(curr.val, end=" -> ")
        curr = curr.next
    print("None")


# 🔹 Create linked list: 1 -> 2 -> 3 -> 4
n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)

n1.next = n2
n2.next = n3
n3.next = n4

head = n1


# 🔹 Run and debug
sol = Solution()

print("Before:")
print_list(head)

new_head = sol.swapPairs(head)

print("After:")
print_list(new_head)