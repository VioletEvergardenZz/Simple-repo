def partiton(list,left,right):
    # 选取第一个元素作为基准值
    tmp=list[left]
    while left<right:
        # 从右向左找到第一个小于基准值的元素
        while left<right and list[right]>=tmp:
            right-=1
        list[left]=list[right]
        # 从左向右找到第一个大于基准值的元素
        while left<right and list[left]<=tmp:
            left+=1
        list[right]=list[left]
    
    # 将基准值放置到最终位置
    list[left]=tmp
    return left

def quick_sort(list,left,right):
    if left<right:
         # 将基准值放置到最终位置
        mid=partiton(list,left,right)
         # 将基准值放置到最终位置
        quick_sort(list,left,mid-1)
        quick_sort(list,mid+1,right)
        
list=[5,4,5,7,2,9,2,4,5,6]
quick_sort(list,0,len(list)-1)
print(list)