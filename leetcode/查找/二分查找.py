'''
给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target
写一个函数搜索 nums 中的 target
如果目标值存在返回下标,否则返回 -1
'''

'''
循环条件 left<right 区间 [left,right)   left和right 指向同一个位置时,循环会停止.无法检查 right 指向的元素，可能会错过目标元素，特别是当目标元素恰好是数组的最后一个元素时。
        left <= right  [left,right] 
'''


class Solution:
    def search(self, nums:list[int], target: int) -> int:
        left,right=0,len(nums)-1      #搜索区间的左右边界
        while left<=right:      #[left,right]   
            m=(left+right)//2   #中值索引

            # 中值与target比较大小
            if nums[m]<target:
                left=m+1
            elif nums[m]>target:
                right=m-1
            else:
                return m
        
        # target不存在
        return -1
    

'''
开区间写法
'''
class Solution:
    def search(self, nums:list[int], target: int) -> int:
        i,j=-1,len(nums)
        while i+1<j:
            m=(i+j)//2
            if nums[m]<target:
                i=m
            elif nums[m]>target:
                j=m
            else:
                return m
        return -1