import json
import unittest
from typing import Optional

from problem_558.solution import Node, Solution


def dict_to_node(d: dict) -> Optional[Node]:
    if d is None:
        return None
    return Node(d['val'], d['isLeaf'],
                dict_to_node(d['topLeft']),
                dict_to_node(d['topRight']),
                dict_to_node(d['bottomLeft']),
                dict_to_node(d['bottomRight']))


class MyTestCase(unittest.TestCase):

    def test1(self):
        node1 = Node(True, True, None, None, None, None)
        node2 = Node(False, True, None, None, None, None)

        solution = Solution()
        node = solution.intersect(node1, node2)

        self.assertEqual(True, node.val)

    def test2(self):
        node1 = Node(False, False, None, None, None, None)
        node2 = Node(False, False, None, None, None, None)

        node1.topLeft = Node(True, True, None, None, None, None)
        node1.topRight = Node(True, True, None, None, None, None)
        node1.bottomLeft = Node(False, True, None, None, None, None)
        node1.bottomRight = Node(False, True, None, None, None, None)

        node2.topLeft = Node(True, True, None, None, None, None)
        node2.topRight = Node(False, False, None, None, None, None)
        node2.bottomLeft = Node(True, True, None, None, None, None)
        node2.bottomRight = Node(False, True, None, None, None, None)

        node2_top_right = node2.topRight
        node2_top_right.topLeft = Node(False, True, None, None, None, None)
        node2_top_right.topRight = Node(False, False, None, None, None, None)
        node2_top_right.bottomLeft = Node(True, True, None, None, None, None)
        node2_top_right.bottomRight = Node(True, True, None, None, None, None)

        solution = Solution()
        node = solution.intersect(node1, node2)

        self.assertIsNotNone(node)

        self.assertTrue(node.topLeft.val)
        self.assertTrue(node.topRight.val)
        self.assertTrue(node.bottomLeft.val)
        self.assertFalse(node.bottomRight.val)

    def test3(self):
        node1 = Node(False, False, None, None, None, None)
        node2 = Node(False, False, None, None, None, None)

        node1.topLeft = Node(False, True, None, None, None, None)
        node1.topRight = Node(False, True, None, None, None, None)
        node1.bottomLeft = Node(True, True, None, None, None, None)
        node1.bottomRight = Node(True, True, None, None, None, None)

        node2.topLeft = Node(True, True, None, None, None, None)
        node2.topRight = Node(True, True, None, None, None, None)
        node2.bottomLeft = Node(True, True, None, None, None, None)
        node2.bottomRight = Node(True, True, None, None, None, None)

        solution = Solution()
        node = solution.intersect(node1, node2)

        self.assertIsNotNone(node)

        self.assertTrue(node.val)
        self.assertTrue(node.isLeaf)

    def test4(self):
        node1 = Node(False, False, None, None, None, None)
        node2 = Node(False, False, None, None, None, None)

        node1.topLeft = Node(False, True, None, None, None, None)
        node1.topRight = Node(False, True, None, None, None, None)
        node1.bottomLeft = Node(False, True, None, None, None, None)
        node1.bottomRight = Node(False, True, None, None, None, None)

        node2.topLeft = Node(False, True, None, None, None, None)
        node2.topRight = Node(False, True, None, None, None, None)
        node2.bottomLeft = Node(False, True, None, None, None, None)
        node2.bottomRight = Node(False, True, None, None, None, None)

        solution = Solution()
        node = solution.intersect(node1, node2)

        self.assertIsNotNone(node)

        self.assertFalse(node.val)
        self.assertTrue(node.isLeaf)

    def test5(self):
        with open('solution_test_5.json') as f:
            res = json.load(f)

        node1 = dict_to_node(res['node1'])
        node2 = dict_to_node(res['node2'])
        result = dict_to_node(res['result'])

        solution = Solution()
        node = solution.intersect(node1, node2)

        self.assertIsNotNone(node)
