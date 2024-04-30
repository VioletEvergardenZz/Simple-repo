# def square_numbers(num):
#     result=[]
#     for i in num:
#         result.append(i*i)
#     return result

# my_nums=square_numbers([1,2,3,4,5])
# print(my_nums)

def square_numbers(num):
    for i in num:
        # 当一个函数包含yield则函数是一个生成器，每当调用这个函数时，就会从yield处返回一个生成值
        yield i*i

my_gen=square_numbers([1,2,3,4,5])
# print(my_gen)

# next函数
print("Running next function: ")
# 生成器每次只生成一个值
print(next(my_gen))
#for循环
print("Then running for loop: ")
for i in my_gen:
    print(i)


# 列表推导式
my_lst=[i*i for i in [1,2,3,4,5]]

# 生成器推导式
my_gen1=(i*i for i in [1,2,3,4,5])
print(my_gen1)