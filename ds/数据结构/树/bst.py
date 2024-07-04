'二叉搜索树(binary search tree)'

class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

class BinarySearchTree:
    # 构造方法
    # 初始化空树
    def __init__(self):
        self._root=None
    
    def search(self,num:int):
        cur=self._root
        while cur is not None:
            # 目标节点在右子树
            if cur.val < num:
                cur=cur.right
            # 目标节点在左子树
            elif cur.val> num:
                cur=cur.left
            else:
                break
        return cur
    

    def insert(self,num:int):
        # 若树为空 初始化根节点
        if self._root is None:
            self._root=TreeNode(num)
            return
        # 循环查找
        cur,pre=self._root,None
        while cur is not None:
            # 查找重复节点 直接返回
            if cur.val==num:
                return
            pre=cur
            # 插入位置在cur的右子树中:
            if cur.val<num:
                cur=cur.right
            # 插入位置在cur的左子树中
            else:
                cur=cur.left
        # 插入节点
        node=TreeNode(num)
        if pre.val<num:
            pre.right=node
        else:
            pre.left=node

    def remove(self,num:int):
        if self._root is None:
            return
        # 查找节点
        cur,pre=self._root,None
        while cur is not None:
            if cur.val ==num:
                break
            pre=cur
            if cur.val<num:
                cur=cur.right
            else:
                cur=cur.left
        if cur is None:
            return
        
        # 子节点数量为0或1
        if cur.left is None or cur.right is None:
            child=cur.left or cur.right
            # 删除节点cur
            if cur != self._root:
                if pre.left==cur:
                    pre.left=child
                else:
                    pre.right=child
            else:
                self._root=child
        
        # 子节点数为2
        else:
            # 获取中序遍历中cur的下一个节点
            tmp: TreeNode = cur.right
            while tmp.left is not None:
                tmp=tmp.left
            # 递归删除节点
            self.remove(tmp.val)
            # 用tmp覆盖cur
            cur.val = tmp.val

if __name__=='__main__':
    bst=BinarySearchTree()
    nums=[4,2,6,7,3,5,1]
    for num in nums:
        bst.insert(num)

# 插入节点
bst.insert(16)

bst.remove(1)
bst.remove(2)
bst.remove(4)
