# 给定一个链表的头节点  head ，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。

class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution(object):
    def detectCycle(self, head:ListNode):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast=slow=head
        # 检测是否有环
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if fast is slow:
                while slow is not head:
                    slow=slow.next
                    head=head.next
                return slow
        return None