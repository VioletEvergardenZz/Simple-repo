'''
给定 pushed 和 popped 两个序列，每个序列中的 值都不重复，
只有当它们可能是在最初空栈上进行的推入 push 和弹出 pop 操作序列的结果时，
返回 true:否则,返回 false
'''
class Solution(object):
    def validateStackSequences(self,pushed:list[int],poped:list[int]):
        stack,i=[],0
        for num in pushed:
            pushed.append(num)
            while stack and stack[-1]==poped[i]:
                stack.pop()
                i+=1
        return not stack