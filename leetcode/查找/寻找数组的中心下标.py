# 数组 中心下标 是数组的一个下标，其左侧所有元素相加的和等于右侧所有元素相加的和。

class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        sum_left,sum_right=0,sum(nums)
        for i in range(len(nums)):
            sum_right-=nums[i]
            if sum_left==sum_right:
                return i
            sum_left+=nums[i]
        return -1