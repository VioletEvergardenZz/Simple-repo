from collections import deque

# 初始化队列
# 在Python中 一般将双向队列类deque当做队列使用
# 虽然 queue.Queue() 是纯正的队列类，但不太好用，因此不推荐

que:deque[int]=deque()

# 元素入队
que.append(1)
que.append(3)
que.append(2)
que.append(5)
que.append(4)
print(f'队列qeu:{que} ')

# 访问队首元素
front:int=que[0]
print("队首元素 front =", front)

# 元素出队
pop:int=que.popleft()
print("出队元素 pop =", pop)
print("出队后 que =", que)

# 获取队列的长度
size=len(que)
print("队列长度 size =", size)

# 判断队列是否为空
is_empty=len(que)==0
print("队列是否为空 =", is_empty)