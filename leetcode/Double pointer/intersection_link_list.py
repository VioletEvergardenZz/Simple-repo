# 寻找两个链表的交点

class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution(object):
    def getIntersectionNode(self,headA:ListNode,headB:ListNode):
        A=headA
        B=headB
        while A!=B:
            # 如果其中一个指针到达链表的末尾,则将其指向另一个链表的头节点,继续向后移动
            # 最终它们要么相遇于交点,要么同时到达链表的末尾
            A=A.next if A else headB
            B=B.next if B else headA
        # 返回A 或 B,它们都指向交点,没有交点,则返回 None
        return A