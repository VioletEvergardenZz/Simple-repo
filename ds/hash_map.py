if __name__=="__main__":
    # 初始化哈希表
    hmap={}

    # 添加操作
    # 在哈希表中添加键值对
    hmap[12836] = "小哈"
    hmap[15937] = "小啰"
    hmap[16750] = "小算"
    hmap[13276] = "小法"
    hmap[10583] = "小鸭"

    # 查询操作
    name=hmap[12836]

    # 删除操作
    hmap.pop(10583)

    # 遍历哈希表
    # 遍历键值对
    for key,value in hmap.items():
        print(key,'->',value)
    # 单独遍历键
    for key in hmap.keys():
        print(key)
    # 单独遍历值
    for value in hmap.values():
        print(value)
    