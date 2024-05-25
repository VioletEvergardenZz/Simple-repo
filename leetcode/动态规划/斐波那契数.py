'''
斐波那契数 （通常用 F(n) 表示）形成的序列称为 斐波那契数列
F(0) = 0,F(1) = 1
F(n) = F(n - 1) + F(n - 2)，其中 n > 1

0, 1, 1, 2, 3, 5, 8, 13, 21, …
0不是第一项,而是第零项。

给定 n ，请计算 F(n) 。
'''


class Solution(object):
    def fib(self,n:int):
        a,b=0,1
        for _ in range(n):   # 循环n次,每次计算下一个斐波那契数
           a,b=b,a+b    # 斐波那契数,下一个斐波那契数的候选值
        return a  # a 是第 n 个斐波那契数
 