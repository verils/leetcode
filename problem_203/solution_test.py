import unittest
from problem_203.solution import ListNode, Solution


class MyTestCase(unittest.TestCase):

    def test1(self):
        head = ListNode(1)
        node1 = head.next = ListNode(2)
        node2 = node1.next = ListNode(6)
        node3 = node2.next = ListNode(3)
        node4 = node3.next = ListNode(4)
        node5 = node4.next = ListNode(5)
        node5.next = ListNode(6)

        new_head = Solution.remove_elements(head, 6)

        self.assertEqual(head, new_head)
        self.assertEqual(1, new_head.val)
        self.assertEqual(2, new_head.next.val)
        self.assertEqual(3, new_head.next.next.val)
        self.assertEqual(4, new_head.next.next.next.val)
        self.assertEqual(5, new_head.next.next.next.next.val)

    def test2(self):
        head = None
        new_head = Solution.remove_elements(head, 1)
        self.assertEqual(head, new_head)

    def test3(self):
        head = ListNode(1)
        new_head = Solution.remove_elements(head, 1)
        self.assertEqual(None, new_head)

    def test4(self):
        head = ListNode(1)
        node1 = head.next = ListNode(2)
        node2 = node1.next = ListNode(2)
        node2.next = ListNode(1)

        new_head = Solution.remove_elements(head, 2)

        self.assertEqual(head, new_head)
        self.assertEqual(1, new_head.val)
        self.assertEqual(1, new_head.next.val)
