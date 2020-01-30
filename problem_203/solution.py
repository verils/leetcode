class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    @staticmethod
    def remove_elements(head: ListNode, val: int) -> ListNode:
        sentinel = ListNode(0)
        sentinel.next = head

        prev, curr = sentinel, sentinel.next
        while curr:
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next

        return sentinel.next
