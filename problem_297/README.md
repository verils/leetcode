# 二叉树的序列化与反序列化

[二叉树的序列化与反序列化](https://leetcode-cn.com/problems/serialize-and-deserialize-binary-tree/)

两种实现方式：递归和队列。其中递归使用DFS模式，队列使用BFS模式

经对比在Python3中队列+循环迭代效率稍高，且在大数量时更安全（避免StackOverflow）

