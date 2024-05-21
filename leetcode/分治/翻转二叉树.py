# Definition for a binary tree node.
# 给你一棵二叉树的根节点 root ，翻转这棵二叉树，并返回其根节点。

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root:TreeNode):
        if not root:return 
        tmp = root.left
        root.left=self.invertTree(root.right)
        root.right=self.invertTree(tmp)
        return root
