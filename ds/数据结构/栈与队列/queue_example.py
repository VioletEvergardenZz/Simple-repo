# producer consumer模型

import threading
import queue

q=queue.Queue()

def consumer(q):
    while True:
        # 阻塞操作
        item=q.get()
        print('Consumer: ',item)
        q.task_done()
        

def producer(q):
    for i in range(10):
        q.put(i)

t1=threading.Thread(target=consumer,args=(q,),daemon=True)
t2=threading.Thread(target=consumer,args=(q,),daemon=True)
t1.start()
t2.start()

producer(q)
q.join()



