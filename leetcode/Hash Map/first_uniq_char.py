# 给定一个字符串 s ，找到 它的第一个不重复的字符，并返回它的索引 。如果不存在，则返回 -1 。

class Solution(object):
    def firstUniqChar(self,s:str):
        dic={}
        for c in s:
            # 判断c是否在字典中 
            dic[c] = not c in dic  # 如果 c 不在字典中，将其添加到字典中，键为 c，值为 True。   
        'enumerate() 函数是一个内置函数，它返回一个迭代器，该迭代器产生包含两个元素的元组序列，其中第一个元素是原始序列中当前位置的索引，第二个元素是当前位置的值。'
        for i,c in enumerate(s):
            if dic[c]:return i    # 如果 c 对应的值为 True，说明它是第一个不重复的字符，返回它的索引 i。
        return -1
    
Solution1=Solution()
res=Solution1.firstUniqChar('aabc')
print(res)