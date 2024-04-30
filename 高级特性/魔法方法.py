# 特殊方法 通常写在类定义里面，用来定义类要如何与py的内置函数和运算符交互

# print(f'{1+2=}')
# print(f'{'a'+'b'=}')

# __add__
# print((x:=1).__add__(2))
# print(('a'.__add__('b')))


from typing import List


class ShoppingCart:
    def __init__(self,items:List[str]):
        self.items=items

    def __add__(self,another_cart):
        new_cart=ShoppingCart(self.items+another_cart.items)
        return new_cart
    
    def __str__(self):
        return f'Cart({self.items})'
    
    def __len__(self):
        return len(self.items)
    
    def __call__(self,item):
        self.items.append(item)

cart1=ShoppingCart(['apple','banana'])
cart2=ShoppingCart(['orange','pear'])
new_cart=cart1+cart2
# 通过实例来调用
new_cart('peach')
new_cart('watermelon')
print(new_cart)
print(len(new_cart))