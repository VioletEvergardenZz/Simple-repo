# 数组 中心下标 是数组的一个下标，其左侧所有元素相加的和等于右侧所有元素相加的和。

class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        sum_left,sum_right=0,sum(nums)
        for i in range(len(nums)):      # 每次循环都是为了判断i是否为中心下标
            sum_right-=nums[i]
            if sum_left==sum_right:     # 第一次判断sum_left为0
                return i                # 返回中心下标
            sum_left+=nums[i]
        return -1