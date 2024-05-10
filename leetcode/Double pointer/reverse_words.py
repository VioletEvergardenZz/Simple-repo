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