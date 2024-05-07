from collections import deque


class TreeNode:
    # 二叉树节点类
    def __init__(self,val:int):
        self.val:int=val
        self.left:TreeNode|None=None
        self.right:TreeNode|None=None


# 层序遍历
def level_order(root:TreeNode|None):
    # 初始化队列，加入根节点
    queue:deque[TreeNode]=deque()
    queue.append(root)
    # 初始化一个列表，用于保存遍历序列
    res=[]
    while queue:
        node:TreeNode|None=queue.popleft()
        res.append(node.val)
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)
    return res

# 深度优先搜索
def pre_order(root:TreeNode|None):
    # 前序遍历
    if root is None:
        return
    res.append(root.val)
    pre_order(root=root.left)
    pre_order(root=root.right)

def in_order(root:TreeNode|None):
    # 中序遍历
    if root is None:
        return
    in_order(root=root.left)
    res.append(root.val)
    in_order(root=root.right)

def post_order(root:TreeNode|None):
    # 后序遍历
    if root is None:
        return
    post_order(root=root.left)
    post_order(root=root.right)
    res.append(root.val) 

if __name__=="__main__":
    # 初始化二叉树
    # 初始化节点
    n1=TreeNode(val=1)
    n2=TreeNode(val=2)
    n3=TreeNode(val=3)
    n4=TreeNode(val=4)
    n5=TreeNode(val=5)

    # 构建节点之间的引用
    n1.left=n2
    n1.right=n3
    n2.left=n4
    n2.right=n5

    # 插入与删除节点
    p=TreeNode(0)
    # 在n1->n2中间插入节点P
    n1.left=p
    p.left=n2
    # 删除节点
    n1.left=n2

    # 层序遍历
    level_order_res=level_order(n1)
    print("层序遍历的节点打印序列 = ", level_order_res)

    # 前序遍历
    res=[]
    pre_order(n1)
    print("\n前序遍历的节点打印序列 = ", res)	
    
    # 中序遍历
    res.clear()
    in_order(n1)
    print("\n中序遍历的节点打印序列 = ", res)

    # 后序遍历
    res.clear()
    post_order(n1)
    print("\n后序遍历的节点打印序列 = ", res)

