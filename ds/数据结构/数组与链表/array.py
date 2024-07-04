import random

# 在数组中访问元素
def random_access(nums:list[int]):
    # 随机索引
    random_index=random.randint(0,len(nums)-1)
    random_num=nums[random_index]
    return random_num

#  插入元素
def insert(nums:list[int],num:int,index:int):
    for i in range(len(nums)-1,index,-1):
        # 数组右移
        nums[i]=nums[i-1]
    # 将 num 赋给 index 处的元素
    nums[index]=num

# 删除索引
def remove(nums:list[int],index:int):
    # 数组左移
    for i in range(index,len(nums)-1):
        nums[i]=nums[i+1]
        # 原先末尾的元素变得“无意义”了，所以无须特意去修改它

#  遍历数组
def traverse(nums:list[int]):
    count=0
    # 索引遍历数组
    for i in range(len(nums)):
        count+=nums[i]
    # 直接遍历数组元素
    for num in nums:
        count+=num
    # 同时遍历索引和元素
    # enumerate函数返回(index, value)序列
    for i,num in enumerate(nums):
        count+=nums[i]
        count+=num

# 查找元素(线性查找)
def find(nums:list[int],target:int):
    for i in range(len(nums)):
        if nums[i]==target:
            return i
    return -1

# 扩容数组
def extend(nums:list[int],enlarge:int):
    res=[0]*(len(nums)+enlarge)
    for i in range(len(nums)):
        res[i]=nums[i]
    return res

if __name__=="__main__":
    # 初始化数组
    nums=[1,3,2,5,4]
    
    print (f'在 nums 中获取随机元素 array nums: {nums}')
    random_num:int=random_access(nums)
    print(random_num)

    insert(nums,6,3)
    print(f'在索引3处插入数字6,得到nums={nums}')

    remove(nums,2)
    print("删除索引 2 处的元素，得到 nums =", nums)

    # 遍历数组
    traverse(nums)

    # 查找元素
    index:int=find(nums,3)
    print(f'在nums中查找元素3,得到索引: {index}')

    # 扩容数组
    extend_nums=extend(nums,3)
    print(f'将数组长度扩展至 8 ，得到 nums = {extend_nums}')