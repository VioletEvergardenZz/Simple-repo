# event loop
# task 显示交换控制权给 event loop 方式:await
 

import asyncio
import time


async def say_after(delay,what):

    # Coroutine -> task
    await asyncio.sleep(delay)
    # print(what)
    return f'{what}-{delay}'


async def main():
    
    # print(f'started at {time.strftime('%X')}')

    # say_after函数调用后返回一个Coroutine
    # await 一个 Coroutine  Coroutine ->task 并且被告诉了event loop 
    # await say_after(1,'hello')
    # await say_after(2 ,'world')
    # print (f'finished at {time.strftime('%X')}')

    # task1=asyncio.create_task(say_after(1,'hello'))
    # task2=asyncio.create_task(say_after(2,'world'))
    print(f'started at {time.strftime('%X')}')

    # await task1
    # await task2
    

    # 拿到Coroutine 返回值需要用到await
    ret=await asyncio.gather(say_after(1,'hello'),say_after(2,'world'))
    print(ret)
    print(f'finished at {time.strftime('%X')}')

#  synchronize变为asynchronize模式的入口
#  把main()作为一个task给放到了event loop，event loop 寻找task
asyncio.run(main())