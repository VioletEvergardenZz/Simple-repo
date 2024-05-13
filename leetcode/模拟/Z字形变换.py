# 将一个给定字符串 s 根据给定的行数 numRows ，以从上往下、从左到右进行 Z 字形排列。

class Solution(object):
    def convert(self,s:str,numRows:int):
        # 只用1行来展示字符串
        if numRows<2:return s

        # res作为一个有numRows个空字符串元素的列表
        res=['' for _ in range(numRows)]
        # flag控制写入字符时行间的移动方向
        i,flag=0,-1
        for c in s:
            res[i]+=c
            if i==0 or i==numRows-1:flag=-flag
            # 根据当前的flag值来更新行索引
            i+=flag

            # ''是一个空字符串，作为连接符
        return ''.join(res)