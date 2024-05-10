# 给定一个字符串 s ，找到 它的第一个不重复的字符，并返回它的索引 。如果不存在，则返回 -1 。

class Solution(object):
    def firstUniqChar(self,s:str):
        dic={}
        for c in s:
            # 判断c是否在字典中
            dic[c] = not c in dic
        for i,c in enumerate(s):
            if dic[c]:return i
        return -1
    
Solution1=Solution()
res=Solution1.firstUniqChar('aabc')
print(res)