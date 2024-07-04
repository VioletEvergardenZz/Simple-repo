class ListNode:
    def __init__(self,val:int):
        self.val:int=val
        self.next:ListNode|None=None  # 指向下一节点的引用

# 插入节点
def insert(node0:ListNode,P:ListNode):
    # 在链表的节点node0之后插入节点P
    node1=node0.next
    P.next=node1
    node0.next=P

# 删除节点
def remove(node0:ListNode):
    # 删除node0节点后的首个节点
    if not node0.next:
        return
    P=node0.next
    node1=P.next
    node0.next=node1

# 访问节点
def access(head:ListNode,index:int):
    # 访问链表中索引为index的节点
    for _ in range(index):
        if not head:
            return None
        head=head.next
    return head

# 查找节点(线性查找)
def find(head:ListNode,target:int):
    index=0
    while head:
        if head.val==target:
            return index
        head=head.next
        index+=1
    return -1

if __name__=="__main__":
    # 初始化链表 1 -> 3 -> 2 -> 5 -> 4
    node0=ListNode(1)
    node1=ListNode(3)
    node2=ListNode(2)
    node3=ListNode(5)
    node4=ListNode(4)
    # 引用
    node0.next=node1
    node1.next=node2
    node2.next=node3
    node3.next=node4

    # 插入节点
    p=ListNode(0)
    insert(node0,p)

    # 删除节点
    remove(node0)

    # 访问节点
    node=access(node0,3)
    print("链表中索引 3 处的节点的值 = {}".format(node.val))

    # 查找节点
    index=find(node0,5)
    print(f'链表中值为2的节点的索引为: {index}')