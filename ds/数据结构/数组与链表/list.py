
if __name__=="__main__":
    # 初始化列表
    # 无初始值
    nums1:list[int]=[]
    # 有初始值
    nums:list[int]=[3,2,1,5,4]

    # 访问元素
    num:int=nums[1]
    # 更新元素
    nums[1]=0

    # 清空列表
    nums.clear()

    # 在尾部添加元素
    nums.append(1)
    nums.append(3)
    nums.append(5)
    nums.append(2)
    nums.append(4)

    # 在中间插入元素
    nums.insert(3,6)   #在索引3处插入数字6
    
    # 删除元素(索引)
    nums.pop(3)
    
    # 通过索引来遍历列表
    count=0
    for i in range(len(nums)):
        count+=nums[i]

    # 直接遍历列表元素
    for num in nums:
        count+=num

    # 拼接列表
    new_nums=[6,7,9,8,10]
    nums+=new_nums

    # 列表排序
    nums.sort()
    print(nums)
