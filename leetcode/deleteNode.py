class ListNode:
    def __init__(self,val):
        self.val=val
        self.next=None

class Solution:
    def deleteNode(self,node:ListNode):
        # node是要删除的节点
        node.val=node.next.val
        node.next=node.next.next
    
