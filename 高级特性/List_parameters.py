from typing import List

# 应避免使用可变对象作为默认参数
# 默认参数作为函数属性，在函数定义时就被定义，而不是在函数调用时定义
# def add_to(num,target:List=[]):
def add_to(num,target=None):
    if not target:
        target=[] 
    print(id(target))
    target.append(num)
    return target

print(add_to(2))
print(add_to(3))

    