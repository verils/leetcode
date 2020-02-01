import json
import unittest

from problem_297.btree import TreeNode
from problem_297.recursion_codec import Codec


class CodecTest(unittest.TestCase):

    def test1(self):
        root = TreeNode(1)

        codec = Codec()
        serialized = codec.serialize(root)

        self.assertEqual('1,,', serialized)

    def test2(self):
        root = TreeNode(1)
        left, right = root.add_children(2, 3)
        right.add_children(4, 5)

        codec = Codec()
        serialized = codec.serialize(root)
        new_root = codec.deserialize(serialized)

        self.assertEqual(root, new_root)

    def test3(self):
        codec = Codec()
        serialized = codec.serialize(None)
        new_root = codec.deserialize(serialized)

        self.assertEqual(None, new_root)

    def test4(self):
        with open('codec_test_4.json') as f:
            arr = json.load(f)

        root = TreeNode.from_array(arr)

        codec = Codec()
        serialized = codec.serialize(root)
        new_root = codec.deserialize(serialized)

        self.assertEqual(root, new_root)

    def test_from_array(self):
        arr = [1, 2, 3, 4, 5]
        root = TreeNode.from_array(arr)


if __name__ == '__main__':
    unittest.main()
