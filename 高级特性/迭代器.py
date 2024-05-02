# python中能够用for循环迭代的对象叫可迭代对象 iterables iterables包含__iter__方法

my_str='xiaoxiao'
my_int=10
# hasattr函数查看一个对象是否有某个属性或方法
# 魔法方法一般用来控制对象要怎样回应python的内置行为
print(hasattr(my_str,'__iter__'))
print(hasattr(my_int,'__iter__'))

# 可迭代对象的__iter__返回迭代器 迭代器的__iter__返回迭代器本身
# for循环获取下一个值使用迭代器的__next__方法
it=iter(my_str)  # my_str.__iter__()
while True:
    try:
        print(next(it))
    except StopIteration:
        break
 

# 迭代器 __iter__和 __next__ 方法
# __next__ 每次调用都要获取下一个迭代器的值 直到没有下一个值 StopIteration异常

# 生成器 迭代器的简单实现  生成器函数和生成器表达式
def generator(n):
    for i in range(n):
        print('before yield')
        # 从yield退出再从yield继续
        yield i
        print('after yield')
gen=generator(3)
print(next(gen))
print('-----')
for i in gen:
    print(i)

def fib_generator():
    cur,nxt=0,1
    while True:
        yield cur
        cur,nxt=nxt,cur+nxt
fib_gen=fib_generator()
for _ in range(10):
    print(next(fib_gen))