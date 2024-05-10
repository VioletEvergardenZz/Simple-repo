# 给你一个字符串 s ，请你反转字符串中 单词 的顺序。

class Solution(object):
    def reverseWords(self,str:str):
        return ' '.join(reversed(str.strip().split()))
    

str=Solution()
result=str.reverseWords('   hello world     ')
print(result)