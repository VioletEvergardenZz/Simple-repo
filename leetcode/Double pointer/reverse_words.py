# 给你一个字符串 s ，请你反转字符串中 单词 的顺序。

class Solution(object):
    def reverseWords(self,str:str):
        '''
        使用 split 将字符串按空格分割成字符串数组；
        使用 reverse 将字符串数组进行反转；
        使用 join 方法将字符串数组拼成一个字符串。
        '''
        return ' '.join(reversed(str.split()))
    

str=Solution()
result=str.reverseWords('   hello world     ')
print(result)


'''
Python中split()函数，具体作用如下：
拆分字符串。通过指定分隔符对字符串进行切片,并返回分割后的字符串列表(list)
'''