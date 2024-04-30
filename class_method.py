# 类变量，类方法，静态方法

class Student:
    # 类变量
    student_num=0
    def __init__(self,name,age):
        self.name=name
        self.age=age
        Student.student_num+=1
    
    # 类方法，通过装饰器进行装饰
    # 类方法的第一个参数需要是类本身，获取类的信息  代替构造方法
    @classmethod
    def add_student(cls,add_num):
        cls.student_num+=add_num
    
    @classmethod
    def from_srting(cls,info):
        name,age=info.split(' ')
        return cls(name,age)
    
    # 静态方法不需要传入参数，不能访问类和实例的私有属性
    # 调用静态方法时，需要通过类进行调用
    @staticmethod
    def name_len(name):
        return len(name)


s1=Student('xiaoxiao',20)
s2=Student.from_srting('xiaoxiao 20')
print(f's2.name: {s2.name},s2.name.len: {Student.name_len(s2.name)}')
print(f'Student.student_num: {Student.student_num}')
