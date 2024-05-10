# 从数组中找出满足相加之和等于目标数 target 的两个数

class Solution(object):
    def twoSum(self,nums,target):
        left=0
        right=len(nums)-1
        
        while True:
            sum=nums[left]+nums[right]
            if sum==target:
                return [left+1,right+1]
            elif sum<target:
                left+=1
            else:
                right-=1

