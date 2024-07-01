


def insertion_sort(nums):
    for i in range(1,len(nums)):
        unsort_1st = nums[i]   # 要插入的元素
        j = i - 1  # 排序区间最后一个元素
        
        while j >= 0 and nums[j] > unsort_1st:
            nums[j+1] = nums[j]
            j -= 1  

        nums[j+1] = unsort_1st

nums=[6,2,9,1,5,9,3,2,0]
insertion_sort(nums)
print(nums)
