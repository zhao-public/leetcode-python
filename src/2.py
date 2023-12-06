from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        head = curr = ListNode()

        n = 0

        while l1 and l2:
            sum = l1.val + l2.val + n
            curr.next = ListNode(sum % 10)

            n = sum // 10
            l1 = l1.next
            l2 = l2.next
            curr = curr.next

        while l1:
            sum = l1.val + n
            curr.next = ListNode(sum % 10)
            n = sum // 10
            l1 = l1.next
            curr = curr.next

        while l2:
            sum = l2.val + n
            curr.next = ListNode(sum % 10)
            n = sum // 10
            l2 = l2.next
            curr = curr.next

        if n:
            curr.next = ListNode(n)

        return head.next
