from collections import deque

deq:deque[int]=deque()

# 元素入队
deq.append(2)
deq.append(5)
deq.append(4)
deq.appendleft(3)  # 添加至队首
deq.appendleft(1)
print("双向队列 deque =", deq)

# 访问元素
front=deq[0]
rear=deq[-1]
print("队首元素 front =", front)
print("队尾元素 rear =", rear)

# 元素出队
pop_front=deq.popleft() #队首元素出队
print("队首出队元素  pop_front =", pop_front)
print("队首出队后 deque =", deq)
pop_rear=deq.pop()
print("队尾出队元素  pop_rear =", pop_rear)
print("队尾出队后 deque =", deq)

# 获取双向队列的长度
size=len(deq)
print("双向队列长度 size =", size)

# 判断双向队列是否为空
is_empty=len(deq)==0
print(f'双向队列是否为空: {is_empty}')