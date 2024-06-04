# 合并两个有序链表

class ListNode:
    def __init__(self,val):
        self.val=val
        self.next=None

def mergeTwoLists(list1:ListNode,list2:ListNode):
    if list1==None:
        return list2
    elif list2==None:
        return list1
    elif list1.val<=list2.val:
        list1.next=mergeTwoLists(list1.next,list2)    # 递归
        # 返回头结点
        return list1
    else:
        list2.next=mergeTwoLists(list1,list2.next)
        return list2
    
# 创建链表1：1 -> 2 -> 4
l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)

# 创建链表2：1 -> 3 -> 4
l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)

# 调用 mergeTwoLists 方法
merged_list = mergeTwoLists(l1,l2)

# 打印合并后的链表
while merged_list:
    print(merged_list.val,end=' ')
    merged_list=merged_list.next