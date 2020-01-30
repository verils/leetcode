from abc import ABCMeta, abstractmethod


class Solution:
    __metaclass__ = ABCMeta

    @abstractmethod
    def num_distinct(self, s: str, t: str) -> int:
        pass
