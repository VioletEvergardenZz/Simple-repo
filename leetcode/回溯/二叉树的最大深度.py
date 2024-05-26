# 给定一个二叉树 root ，返回其最大深度。
# 二叉树的 最大深度 是指从根节点到最远叶子节点的最长路径上的节点数。


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        '终止条件: root为空时 返回深度0'
        if not root:return 0
        
        '''
        递推
        计算节点root的左子树深度 调用maxDepth(root.left)
        计算节点root的右子树深度 调用maxDepth(root.right)

        返回值: 树的深度
        '''
        return max(self.maxDepth(root.left),self.maxDepth(root.right))+1