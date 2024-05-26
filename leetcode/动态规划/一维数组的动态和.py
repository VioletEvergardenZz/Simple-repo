'''
输入:nums = [1,1,1,1,1]
输出:[1,2,3,4,5]
解释:动态和计算过程为 [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1] 。
'''

'''
初始状态: f(0)=num[0]
转移方程: f(i)=f(i-1)+num[i]
'''

class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        dp=[0]*len(nums)
        dp[0]=nums[0]
        for i in range(1,len(nums)):
            dp[i]=dp[i-1]+nums[i]
        return dp