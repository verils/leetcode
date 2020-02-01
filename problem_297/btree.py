class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __eq__(self, other):
        return self.__dict__ == other.__dict__ \
            if self and other \
            else not self and not other

    def add_children(self, left_val, right_val):
        self.left = TreeNode(left_val)
        self.right = TreeNode(right_val)
        return self.left, self.right

    @classmethod
    def from_array(cls, arr: list):
        return cls._create_node(arr, 1)

    @classmethod
    def _create_node(cls, arr: list, index: int):
        if index > len(arr):
            return None
        if not arr[index - 1]:
            return None

        node = TreeNode(int(arr[index - 1]))
        node.left = cls._create_node(arr, index * 2)
        node.right = cls._create_node(arr, index * 2 + 1)
        return node
