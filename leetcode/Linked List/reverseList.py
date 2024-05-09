class ListNode:
    def __init__(self,val):
        self.val=val
        self.next=None

def reverseList(list:ListNode,head:ListNode):
    left,right=head,None
    while left:
        tmp=left.next
        left.next=right
        right=left
        left=tmp
    return right

l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)

# 调用 reverseList 方法
reverse = reverseList(l1, l1)
# 打印反转后的链表的值
while reverse:
    print(reverse.val, end=' ')
    reverse = reverse.next