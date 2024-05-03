def f(a,b=3,*args,**kwargs):
    print(a+b)

code=f.__code__

print(code.co_argcount)
print(code.co_posonlyargcount)
print(code.co_kwonlyargcount)

f(1)
f(1,1)
f(a=1)