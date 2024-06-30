'冒泡排序'

def bubble_sort(nums):
    for i in range(0,len(nums)-1):
        for j in range(0,len(nums)-1-i):
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1]=nums[j+1],nums[j]

nums=[2,9,4,7,1,4,0,3,5,8]
bubble_sort(nums)
print(nums)