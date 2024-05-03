import atexit
import os

# f=atexit.register(f)
@atexit.register
def f():
    print('exiting')

# atexit.register(f,'exiting')

atexit.unregister(f)

class MyFunc:
    def __call__(self):
        print('exiting')
    def __eq__(self,other):
        if isinstance(other,MyFunc):
            return True
        return False
f0=MyFunc()
atexit.register(f0)
# f1=MyFunc()
# atexit.unregister(f1)

# print(atexit._ncallbacks())
# atexit._clear()
# atexit._run_exitfuncs()
# print('Before exit')

os._exit(0)