'''
为了删除节点 node ，可使用以下方法：

复制后继节点 node.next 的「节点值」至节点 node 
将 node.next 从链表中删除
'''

class ListNode:
    def __init__(self,val):
        self.val=val
        self.next=None

class Solution:
    def deleteNode(self,node:ListNode):
        # node是要删除的节点
        node.val=node.next.val       
        node.next=node.next.next
    
