from problem_297.btree import TreeNode


class Codec:

    def serialize(self, root: TreeNode) -> str:
        def _serialize(arr: list, node: TreeNode):
            if not node:
                return arr.append('')

            arr.append(str(node.val))
            _serialize(arr, node.left)
            _serialize(arr, node.right)

        res = []
        _serialize(res, root)
        return ','.join(res)

    def deserialize(self, data: str) -> TreeNode:
        def _deserialize(arr: list, cursor: int) -> (TreeNode, int):
            if arr[cursor] == '':
                return None, cursor + 1

            node = TreeNode(int(arr[cursor]))
            cursor += 1
            node.left, cursor = _deserialize(arr, cursor)
            node.right, cursor = _deserialize(arr, cursor)
            return node, cursor

        root, count = _deserialize(data.split(','), 0)
        return root
