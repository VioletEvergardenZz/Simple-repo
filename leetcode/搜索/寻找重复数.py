'''
给定一个包含 n + 1 个整数的数组 nums ，其数字都在 [1, n] 范围内(包括 1 和 n),可知至少存在一个重复的整数。
假设 nums 只有 一个重复的整数 ，返回 这个重复的数 。
'''

class Solution(object):
    def findDuplicate(self,nums:list[int]):
        hmap=set()
        for num in nums:
            if num in hmap:return num
            hmap.add(num)
        return -1