import time

def timeit(f):
    def wrapper(*args,**kwargs):
        start=time.time()
        ret=f(*args,**kwargs)
        print(time.time()-start)
        return ret

    return wrapper


@timeit
def my_func(x):
    time.sleep(x)

@timeit
def add(x,y):
    return x+y


print(add(2,3)) 



