'''
归并排序的关键在于利用递归的分治策略，将原始数组划分成越来越小的子数组，
直到每个子数组只有一个元素或为空。然后通过合并操作，
将这些有序的子数组逐步合并成更大的有序数组，直到整个数组排序完成。
'''

# 划分
def merge_sort(nums):
    if len(nums) <= 1:
        return nums

    mid = len(nums) // 2
    left_half = merge_sort(nums[:mid])
    rigth_half = merge_sort(nums[mid:])

    return merge(left_half,rigth_half)

# 合并
def merge(left,right):
    sorted_nums = []
    left_index,right_index = 0, 0

    # 合并两个子数组
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            sorted_nums.append(left[left_index])
            left_index += 1
        else:
            sorted_nums.append(right[right_index])
            right_index += 1

    # 处理剩余元素 extend 逐个添加元素
    if left_index < len(left):
        sorted_nums.extend(left[left_index:])
    if right_index < len(right):
        sorted_nums.extend(right[right_index:])
    
    return sorted_nums

nums = [4,7,1,3,0,2,8,5]
print(nums)
sorted_nums = merge_sort(nums)
print(sorted_nums)