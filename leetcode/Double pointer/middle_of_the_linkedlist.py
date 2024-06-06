# 链表的中间节点
# 快慢指针
class ListNode(object):
    def __init__(self,val):
        self.val=val
        self.next=None


'快指针走两步 慢指针走一步'
class Solution(object):
    def middleNode(self,head):
        slow=fast=head

        '链表长度为奇数或偶数'
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        return slow