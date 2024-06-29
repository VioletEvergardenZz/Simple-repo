'不断找到数组中的最小元素并将其放到已排序区间的末尾'

def selection_sort(nums:list[int]):
    n=len(nums)

    '使用 range(n)，则在 i 达到 n-1 时，再次运行外循环没有意义'
    for i in range(n-1):
        k = i
        for j in range(i+1,n):
            if nums[j]<nums[k]:
                k=j
        nums[i],nums[k]=nums[k],nums[i]
