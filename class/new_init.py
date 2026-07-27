class Person:
    def __new__(cls, name):
        print("1. __new__ 被调用：分配内存，生成实例")
        # 必须调用父类 object.__new__ 来真正创建对象
        instance = super().__new__(cls)
        return instance  # 把创建好的实例返回出去

    def __init__(self, name):
        print("2. __init__ 被调用：拿到了 __new__ 给的 self，开始赋值")
        self.name = name

p = Person("Alice")



# Singleton
class Database:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            # 第一次实例化，调用父类创建对象
            cls._instance = super().__new__(cls)
        return cls._instance # 以后每次都返回同一个对象


# 需求：创建一个大写字符串类，传入小写自动变大写
class UpperStr(str):
    def __new__(cls, value):
        # 在对象创建前修改传入的值
        uppercase_value = value.upper()
        return super().__new__(cls, uppercase_value)

s = UpperStr("hello")
print(s)  # 输出: HELLO


