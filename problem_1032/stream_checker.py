from typing import List


class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie_tree_root = {}
        self.query_history = ''
        for word in words:
            tree_node = self.trie_tree_root
            reversed_word = word[::-1]
            for ch in reversed_word:
                tree_node = tree_node.setdefault(ch, {})
            tree_node['lf'] = True

    def query(self, letter: str) -> bool:
        self.query_history = letter + self.query_history

        tree_node = self.trie_tree_root
        for ch in self.query_history:
            tree_node = tree_node.get(ch)
            if tree_node is None:
                return False
            if tree_node.get('lf'):
                return True
        return False
