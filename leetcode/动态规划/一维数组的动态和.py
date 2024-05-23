class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        dp=[0]*len(nums)
        dp[0]=nums[0]
        for i in range(1,len(nums)):
            dp[i]=dp[i-1]+nums[i]
        return dp