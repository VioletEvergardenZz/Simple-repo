class Solution(object):
    def fib(self,n:int):
        a,b=0,1
        for _ in range(n):
        # 后面的每一项数字都是前面两项数字的和
           a,b=b,a+b
        return a
 