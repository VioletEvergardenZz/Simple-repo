# 链表的中间节点
# 快慢指针
class ListNode(object):
    def __init__(self,val):
        self.val=val
        self.next=None

class Solution(object):
    def middleNode(self,head):
        slow=fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        return slow