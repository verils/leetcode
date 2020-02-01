from collections import deque

from problem_297.btree import TreeNode


class Codec:

    def serialize(self, root: TreeNode) -> str:
        res = []
        q = deque([root])
        while q:
            node = q.popleft()
            if node is None:
                res.append('')
                continue

            res.append(str(node.val))
            q.append(node.left)
            q.append(node.right)
        return ','.join(res)

    def deserialize(self, data: str) -> TreeNode:
        arr = data.split(',')
        if arr[0] == '':
            return None

        nodes = [TreeNode(int(v)) if v != '' else None for v in arr]
        nodes_len = len(nodes)
        cursor = 1
        for i, node in enumerate(nodes):
            if cursor > nodes_len:
                break
            if not node:
                continue
            node.left = nodes[cursor]
            node.right = nodes[cursor + 1]
            cursor += 2

        return nodes[0]
