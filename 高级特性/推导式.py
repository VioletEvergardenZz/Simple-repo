num=[1,2,3,4,5]

# my_list=[]
# for i in num:
#     my_list.append(i)
# print (my_list)

my_list=[i**2 if i%2==0 else i**3 for i in num]
print(my_list)

letters=['a','b','c']
nums=[1,2,3]
my_list1=[(i,j) for i in letters for j in nums]
print(my_list1)

my_dict={}
# zip函数: 将两个列表的元素以一对应，返回一个元组构成的可迭代对象 
# for i,j in zip(letters,nums):
#     my_dict[i]=j
# print(my_dict)
my_dict={i:j for i,j in zip(letters,nums)}
print(my_dict)


l=[1,2,3,4,5,5,5,6]
# my_set=set()
# for i in l:
#     my_set.add(i)
# print(my_set)


# 与列表推导不同 变为{ }
my_set={i for i in l}
print(my_set)