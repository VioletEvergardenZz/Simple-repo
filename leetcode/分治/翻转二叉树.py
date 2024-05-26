# Definition for a binary tree node.
# 给你一棵二叉树的根节点 root ，翻转这棵二叉树，并返回其根节点。

'''
解决二叉树 第一先想到用递归解决
'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


'以递归交换左右子树完成'
class Solution1:
    def  invertTree(self, root:TreeNode):
        '递归函数终止条件'
        if not root:
            return None
        '将当前节点的左右子树交换'
        root.left,root.right=root.right,root.left
        '递归交换当前节点的左右子树'
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root


class Solution2:
    def invertTree(self, root:TreeNode):
        if not root:return 
        tmp = root.left
        root.left=self.invertTree(root.right)
        root.right=self.invertTree(tmp)
        return root
