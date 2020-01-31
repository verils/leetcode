class Node:
    def __init__(self, val=None, isLeaf=None, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

    def __decode__(self):
        pass


class Solution:

    def intersect(self, node1: 'Node', node2: 'Node') -> 'Node':
        if node1.isLeaf:
            if node1.val:
                return node1
            else:
                return node2

        if node2.isLeaf:
            if node2.val:
                return node2
            else:
                return node1

        node1.topLeft = self.intersect(node1.topLeft, node2.topLeft)
        node1.topRight = self.intersect(node1.topRight, node2.topRight)
        node1.bottomLeft = self.intersect(node1.bottomLeft, node2.bottomLeft)
        node1.bottomRight = self.intersect(node1.bottomRight, node2.bottomRight)

        if node1.isLeaf:
            return node1

        if self._is_all_leaf(node1):
            if self._is_all_true(node1):
                node1 = Node(True, True, None, None, None, None)
            elif self._is_all_false(node1):
                node1 = Node(False, True, None, None, None, None)
        return node1

    @staticmethod
    def _is_all_leaf(node: 'Node') -> bool:
        return True if node.topLeft and node.topLeft.isLeaf and \
                       node.topRight and node.topRight.isLeaf and \
                       node.bottomLeft and node.bottomLeft.isLeaf and \
                       node.bottomRight and node.bottomRight.isLeaf else False

    @staticmethod
    def _is_all_true(node: 'Node') -> bool:
        return True if node.topLeft.val and \
                       node.topRight.val and \
                       node.bottomLeft.val and \
                       node.bottomRight.val else False

    @staticmethod
    def _is_all_false(node: 'Node') -> bool:
        return True if not node.topLeft.val and \
                       not node.topRight.val and \
                       not node.bottomLeft.val and \
                       not node.bottomRight.val else False
