# 给定一个大小为 n 的数组 nums ，返回其中的多数元素。多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        votes=0
        for num in nums:
            if votes==0:x=num
            votes+=1 if num==x else -1
        return x