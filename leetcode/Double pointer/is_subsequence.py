class Solution(object):
    # 判断s是否为t的子序列
    def isSubsequence(self,s,t):
        n,m=len(s),len(t)
        i=j=0
        # 双指针循环判断
        while i<n and j<m:
            if s[i]==t[j]:
                i+=1
            j+=1
        return i==n