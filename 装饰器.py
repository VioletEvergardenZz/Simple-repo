import time
import functools
# def square(x):
#     return x*x
# def print_running(f,x):
#     print(f'{f.__name__} is running ')
#     return f(x)

# result=print_running(square,2)
# print(result)

def decorator(func):
    #wrappre作为代替func的新函数
    def wrapper(*args,**kwargs):
        start_time=time.time()
        result=func(*args,**kwargs)
        end_time=time.time()
        print(f'{func.__name__} execution time: {end_time-start_time} seconds')
        return result
    return wrapper

#square是decorator装饰square函数后的函数,装饰后的函数用来代替原来的函数
#square=decorator(square)
@decorator
def square(x):
    return x*x
square(10)

# 定义装饰器的函数，装饰器生成器
# 装饰器生成器会根据参数生成不同的装饰器
def timer(threshold):
    #生成装饰器
    def decorator(func):
        #wrapper继承func的属性
        @functools.wraps(func)
        def wraapper(*args,**kwargs):
            start_time=time.time()
            result=func(*args,**kwargs)
            end_time=time.time()
            if end_time-start_time>threshold:
                print(f'{func.__name__} took longer than {threshold} seconds')
            return result
        return wraapper
    return decorator


# timer是一个返回装饰器的函数
# sleep_04=timer(0.2)(sleep_04)
@timer(0.2)
def sleep_04():
    time.sleep(0.4)
sleep_04()
print(sleep_04.__name__)
