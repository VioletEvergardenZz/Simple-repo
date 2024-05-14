'''
给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target
写一个函数搜索 nums 中的 target
如果目标值存在返回下标,否则返回 -1
'''

class Solution:
    def search(self, nums:list[int], target: int) -> int:
        left,right=0,len(nums)-1
        while left<=right:
            m=(left+right)//2
            if nums[m]<target:
                left=m+1
            elif nums[m]>target:
                right=m-1
            else:
                return m
        return -1