# 给定两个字符串, s 和 goal。如果在若干次旋转操作之后，s 能变成 goal ，那么返回 true 。
's 的 旋转操作 就是将 s 最左边的字符移动到最右边。 '



class Solution(object):
    def rotateString(self,s,goal):
        return len(s)==len(goal) and s in (goal+goal)   # 拼接字符串goal goal 中包含原字符串 s