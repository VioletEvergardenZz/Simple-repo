# 给你二叉树的根节点 root ，返回其节点值的 层序遍历 。 （即逐层地，从左到右访问所有节点）。

import collections
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def levelOrder(self,root:TreeNode):
        queue=collections.deque()
        res=[]
        queue.append(root)
        while queue:
            tmp=[]
            for _ in range(len(queue)):
                node:TreeNode=queue.popleft()
                # 插入node的值
                tmp.append(node.val)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            res.append(tmp)
        return res