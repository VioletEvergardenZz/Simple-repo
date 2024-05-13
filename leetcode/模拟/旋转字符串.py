# 给定两个字符串, s 和 goal。如果在若干次旋转操作之后，s 能变成 goal ，那么返回 true 。

class Solution(object):
    def rotateString(self,s,goal):
        return len(s)==len(goal) and s in (goal+goal)