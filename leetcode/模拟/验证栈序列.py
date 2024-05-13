class Solution(object):
    def validateStackSequences(self,pushed:list[int],poped:list[int]):
        stack,i=[],0
        for num in pushed:
            pushed.append(num)
            while stack and stack[-1]==poped[i]:
                stack.pop()
                i+=1
        return not stack