# 给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。


from collections import defaultdict


class Solution(object):
    def isAnagram(self,s:str,t:str):
        if len(s)!=len(t):
            return False
        dic=defaultdict(int)
        for c in s:
            dic[c]+=1
        for c in t:
            dic[c]-=1
        for val in dic.values():
            if dic[val]!=0:
                return False
        return True