class Person:
    def __init__(self, age):
        # 赋值时会直接触发 @age.setter
        self.age = age  

    # 1. Getter 装饰器：定义获取属性时的逻辑
    @property
    def age(self):
        print("正在读取 age...")
        return self._age  # 约定俗成：用单下划线 _age 存放真正的私有数据

    # 2. Setter 装饰器：定义设置属性时的逻辑
    @age.setter
    def age(self, value):
        print("正在设置 age...")
        if value < 0:
            raise ValueError("年龄不能为负数！")
        self._age = value

# ===== 外部调用体验 =====
p = Person(20)      # 触发 @age.setter，输出："正在设置 age..."
print(p.age)        # 触发 Getter，输出："正在读取 age..." -> 20
# p.age = -5          # 触发 Setter -> 抛出 ValueError



# 1. 定义一个“非负数校验”描述符类
class NonNegative:
    def __init__(self, name):
        self.name = name

    # 拦截获取值逻辑：instance 是宿主类的实例（如 Student 实例）
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.name, 0)

    # 拦截赋值逻辑
    def __set__(self, instance, value):
        if value < 0:
            raise ValueError(f"{self.name} 不能为负数！")
        instance.__dict__[self.name] = value


# 2. 在宿主类中使用描述符
class Student:
    # age 和 score 都是 NonNegative 类的实例！
    age = NonNegative("age")
    score = NonNegative("score")

# ===== 外部调用 =====
s = Student()
s.age = 18       # 触发 NonNegative.__set__
s.score = 95     # 触发 NonNegative.__set__
# s.score = -10  # 触发 NonNegative.__set__ -> 抛出异常



class SafeDict:
    def __init__(self, name):
        self.name = name

    def __getattr__(self, name):
        # 试图读取不存在的属性时，不报错，而是返回默认提示
        return f"属性 '{name}' 不存在！"

    def __setattr__(self, name, value):
        print(f"日志记录：设置属性 {name} = {value}")
        # 【极其重要】千万不能写 self.name = value，这会无限递归调用 __setattr__ 导致栈溢出！
        # 正确做法：调用父类 object 的 __setattr__
        super().__setattr__(name, value)

obj = SafeDict("Alice")
obj.name = "Toby"  # 输出：日志记录：设置属性 name = Toby
print(obj.unknown)  # 输出：属性 'unknown' 不存在！
