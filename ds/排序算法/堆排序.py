
def sift(nums,low,high):
    
    '''
    nums: 列表
    low: 堆的根节点位置
    high: 堆的最后一个元素的位置
    '''

    i = low
    j = 2 * i + 1
    tmp = nums[low] # 暂存堆顶
    while j <= high:
        if j+1 <= high and nums[j+1] > nums[j]:
            j = j + 1
        if nums[j] > tmp:
            nums[i] = nums[j]
            i = j
            j = 2 * i + 1
        else:   # 如果 tmp 更大
            nums[i] = tmp
            break
    else:
        nums[i] = tmp

def heap_sort(nums):
    n = len(nums)
    for i in range((n-2)//2,-1,-1):
        # i 表示建堆的时候调整的部分的根的下标
        sift(nums,i,n-1)
    # 建堆完成了

    for i in range(n-1,-1,-1):
        # i 指向当前堆的最后一个元素
        nums[0],nums[i] = nums[i],nums[0]
        sift(nums,0,i-1)  # i - 1 是新的 high

nums = [i for i in range(20)]
import random
random.shuffle(nums)
print(nums)
heap_sort(nums)
print(nums)